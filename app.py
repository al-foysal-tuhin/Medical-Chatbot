from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

from src.helper import download_hugging_face_embeddings
from src.prompt import system_prompt

from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)

print("Starting Medical Chatbot...", flush=True)

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

print("Google key exists:", bool(GOOGLE_API_KEY), flush=True)
print("Pinecone key exists:", bool(PINECONE_API_KEY), flush=True)

rag_chain = None


def get_rag_chain():
    global rag_chain

    if rag_chain is None:
        print("Loading embeddings...", flush=True)

        embeddings = download_hugging_face_embeddings()

        print("Embeddings loaded.", flush=True)

        print("Connecting to Pinecone...", flush=True)

        docsearch = PineconeVectorStore.from_existing_index(
            index_name="medical-chatbot",
            embedding=embeddings,
        )

        print("Connected to Pinecone.", flush=True)

        retriever = docsearch.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 3},
        )

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=GOOGLE_API_KEY,
            temperature=0,
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )

        question_answer_chain = create_stuff_documents_chain(llm, prompt)

        rag_chain = create_retrieval_chain(
            retriever,
            question_answer_chain,
        )

        print("RAG initialized.", flush=True)

    return rag_chain


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]

    print("Question:", msg, flush=True)

    chain = get_rag_chain()

    response = chain.invoke({"input": msg})

    print("Answer generated.", flush=True)

    return str(response["answer"])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))

    print(f"Running on port {port}", flush=True)

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
    )