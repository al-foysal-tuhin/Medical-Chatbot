from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

from src.helper import download_hugging_face_embeddings
from src.prompt import system_prompt

from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


# =========================================================
# Flask application
# =========================================================

app = Flask(__name__)

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

print("Starting Medical Chatbot...", flush=True)
print("Google key exists:", bool(GOOGLE_API_KEY), flush=True)
print("Pinecone key exists:", bool(PINECONE_API_KEY), flush=True)


# =========================================================
# Medical knowledge source
# =========================================================

BOOK_TITLE = "Gale Encyclopedia of Medicine 2"


# =========================================================
# Global RAG chain
# =========================================================

rag_chain = None


# =========================================================
# Conversational responses
# =========================================================

def get_conversational_response(message):

    query = message.strip().lower()

    # -----------------------------------------------------
    # Greetings
    # -----------------------------------------------------

    greetings = {
        "hi",
        "hello",
        "hey",
        "hi there",
        "hello there",
        "hey there",
        "good morning",
        "good afternoon",
        "good evening",
    }

    # -----------------------------------------------------
    # Identity questions
    # -----------------------------------------------------

    identity_questions = {
        "who are you",
        "who are you?",
        "what are you",
        "what are you?",
    }

    # -----------------------------------------------------
    # Capability questions
    # -----------------------------------------------------

    capability_questions = {
        "what can you do",
        "what can you do?",
        "how can you help me",
        "how can you help me?",
    }

    # -----------------------------------------------------
    # Source questions
    # -----------------------------------------------------

    source_questions = {
        "what is your source",
        "what is your source?",
        "what is your knowledge source",
        "what is your knowledge source?",
        "what book do you use",
        "what book do you use?",
        "what is the source of your information",
        "where does your information come from",
        "where does your information come from?",
    }

    # -----------------------------------------------------
    # Thanks
    # -----------------------------------------------------

    thanks = {
        "thanks",
        "thanks!",
        "thank you",
        "thank you!",
        "thx",
    }

    # -----------------------------------------------------
    # Greeting response
    # -----------------------------------------------------

    if query in greetings:

        return (
            "Hello! 👋 I'm your Medical AI Assistant.\n\n"
            "I can help you explore general medical information "
            "from my medical knowledge base.\n\n"
            "Try asking me about symptoms, causes, medical "
            "conditions, diagnosis, or treatment information."
        )

    # -----------------------------------------------------
    # Identity response
    # -----------------------------------------------------

    if query in identity_questions:

        return (
            "I'm a Medical AI Assistant powered by a "
            "Retrieval-Augmented Generation (RAG) system.\n\n"
            "I retrieve relevant information from my medical "
            "knowledge base and use an AI language model to "
            "generate an answer based on that information."
        )

    # -----------------------------------------------------
    # Capability response
    # -----------------------------------------------------

    if query in capability_questions:

        return (
            "I can help you explore general medical information, "
            "including:\n\n"
            "• Medical conditions and diseases\n"
            "• Symptoms and signs\n"
            "• Causes and risk factors\n"
            "• Diagnosis and medical tests\n"
            "• General treatment information\n"
            "• Medications and related information\n\n"
            "Example questions:\n\n"
            "• What are the symptoms of diabetes?\n"
            "• What causes acne?\n"
            "• What is hypertension?\n"
            "• What are the symptoms of asthma?\n"
            "• What is anxiety?\n"
            "• What is a BUN test?"
        )

    # -----------------------------------------------------
    # Knowledge-source response
    # -----------------------------------------------------

    if query in source_questions:

        return (
            f"My primary medical knowledge source is:\n\n"
            f"📚 {BOOK_TITLE}\n\n"
            "The book is used as the source material for the "
            "Retrieval-Augmented Generation (RAG) system. "
            "When you ask a medical question, the system "
            "retrieves relevant information from this knowledge "
            "base before generating an answer."
        )

    # -----------------------------------------------------
    # Thank-you response
    # -----------------------------------------------------

    if query in thanks:

        return "You're welcome! 😊 I'm happy to help."

    # -----------------------------------------------------
    # Not a conversational query
    # -----------------------------------------------------

    return None


# =========================================================
# Build RAG chain
# =========================================================

def get_rag_chain():

    global rag_chain

    # Avoid rebuilding the RAG chain for every request
    if rag_chain is not None:
        return rag_chain

    print("Loading embeddings...", flush=True)

    embeddings = download_hugging_face_embeddings()

    print("Embeddings loaded.", flush=True)

    # -----------------------------------------------------
    # Connect to Pinecone
    # -----------------------------------------------------

    print("Connecting to Pinecone...", flush=True)

    docsearch = PineconeVectorStore.from_existing_index(
        index_name="medical-chatbot",
        embedding=embeddings
    )

    print("Connected to Pinecone.", flush=True)

    # -----------------------------------------------------
    # Retriever
    # -----------------------------------------------------

    retriever = docsearch.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 3
        }
    )

    # -----------------------------------------------------
    # Gemini
    # -----------------------------------------------------

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite",
        google_api_key=GOOGLE_API_KEY,
        temperature=0
    )

    # -----------------------------------------------------
    # Prompt
    # -----------------------------------------------------

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt
            ),
            (
                "human",
                "{input}"
            )
        ]
    )

    # -----------------------------------------------------
    # Format retrieved documents
    # -----------------------------------------------------

    def format_docs(docs):

        return "\n\n".join(
            doc.page_content
            for doc in docs
        )

    # -----------------------------------------------------
    # Modern LangChain 1.x RAG chain
    # -----------------------------------------------------

    rag_chain = (
        {
            "context": retriever | format_docs,
            "input": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    print("RAG chain initialized.", flush=True)

    return rag_chain


# =========================================================
# Home page
# =========================================================

@app.route("/")
def index():

    return render_template("chat.html")


# =========================================================
# Chat endpoint
# =========================================================

@app.route("/get", methods=["GET", "POST"])
def chat():

    # -----------------------------------------------------
    # Get user message
    # -----------------------------------------------------

    msg = request.form.get("msg", "").strip()

    if not msg:

        return (
            "Please enter a question so I can help you."
        )

    print("User question:", msg, flush=True)

    # -----------------------------------------------------
    # Handle normal conversation first
    # -----------------------------------------------------

    conversational_response = get_conversational_response(msg)

    if conversational_response is not None:

        print(
            "Handled as conversational input.",
            flush=True
        )

        return conversational_response

    # -----------------------------------------------------
    # Otherwise use RAG
    # -----------------------------------------------------

    try:

        chain = get_rag_chain()

        answer = chain.invoke(msg)

        print("RAG answer generated.", flush=True)

        return str(answer)

    except Exception as e:

        print(
            f"Error while generating response: {e}",
            flush=True
        )

        return (
            "I'm sorry, but I couldn't process your question "
            "right now. Please try again."
        )


# =========================================================
# Run application
# =========================================================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            8080
        )
    )

    print(
        f"Running Medical Chatbot on port {port}",
        flush=True
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )