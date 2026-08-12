# 🩺 Medical Chatbot
### Retrieval-Augmented Generation with LangChain, Pinecone, Google Gemini & Flask

<p align="center">
  <strong>An end-to-end AI medical question-answering system powered by RAG.</strong><br>
  Retrieve relevant medical knowledge from documents, search it with Pinecone,<br>
  and generate grounded responses using Google Gemini.
</p>

<p align="center">
  <a href="https://medical-chatbot-rag.fly.dev/">
    <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Visit%20App-00C853?style=for-the-badge" alt="Live Demo">
  </a>
  <a href="https://github.com/al-foysal-tuhin/Medical-Chatbot">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=flat-square">
  <img src="https://img.shields.io/badge/Google-Gemini-4285F4?style=flat-square&logo=google">
  <img src="https://img.shields.io/badge/Pinecone-Vector%20DB-000000?style=flat-square">
  <img src="https://img.shields.io/badge/Flask-Web%20App-000000?style=flat-square&logo=flask">
  <img src="https://img.shields.io/badge/Fly.io-Deployed-8B5CF6?style=flat-square">
</p>

---

## 🌐 Live Demo

### 👉 [Open the Medical Chatbot](https://medical-chatbot-rag.fly.dev/)

The application is deployed on **Fly.io** and provides a web-based interface where users can ask questions and receive answers generated through a Retrieval-Augmented Generation pipeline.

> ⏳ **First request may take longer:**  
> Fly.io may automatically stop an idle machine. When the application receives a new request, the machine may need to start again. The first request can therefore take longer, especially while the embedding model and RAG components are initialized. Subsequent requests are significantly faster.

> ⚠️ **Medical Disclaimer:**  
> This project is an educational demonstration of RAG and LLM technology. It is **not a medical professional, diagnostic system, or substitute for advice from a qualified healthcare professional.**

---

# ✨ What This Project Does

This project demonstrates how a modern **Retrieval-Augmented Generation (RAG)** application can be built from the ground up.

Instead of relying only on the language model's internal knowledge, the chatbot first retrieves relevant information from a medical knowledge base and then provides that information to **Google Gemini** as context.

The result is a pipeline that combines:

**Medical Documents → Embeddings → Pinecone → Retrieval → Gemini → Answer**

### 🎯 Main Goals

- Build a complete RAG application
- Work with real medical PDF documents
- Generate semantic embeddings
- Store and search vectors using Pinecone
- Integrate Google Gemini with LangChain
- Build a web interface using Flask
- Containerize and deploy the application
- Manage API credentials securely
- Demonstrate an end-to-end AI/ML deployment workflow

---

# 🧠 How the System Works

The chatbot uses the following architecture:

    ┌───────────────────────────────┐
    │       Medical PDF Files      │
    └───────────────┬───────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │       PDF Document Loader      │
    └───────────────┬───────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │         Text Splitter          │
    └───────────────┬───────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │ Hugging Face Sentence          │
    │ Transformer Embeddings         │
    └───────────────┬───────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │        Pinecone Vector DB      │
    └───────────────┬───────────────┘
                    │
                    │
    ┌───────────────▼───────────────┐
    │        User Question           │
    └───────────────┬───────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │      Semantic Retrieval        │
    └───────────────┬───────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │      Relevant Context          │
    └───────────────┬───────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │        Google Gemini           │
    │       Response Generation      │
    └───────────────┬───────────────┘
                    │
                    ▼
    ┌───────────────────────────────┐
    │        Flask Web Interface     │
    └───────────────────────────────┘

---

# 🔄 RAG Pipeline

The complete workflow can be summarized in eight stages:

### 01 — 📄 Document Loading

Medical PDF documents are loaded from the `data/` directory.

### 02 — ✂️ Text Splitting

Large documents are divided into smaller chunks so that individual pieces of information can be efficiently searched.

### 03 — 🧠 Embedding Generation

Each document chunk is converted into a numerical vector using a Hugging Face sentence-transformer model.

### 04 — 🗄️ Vector Storage

The generated vectors are stored in a Pinecone index.

### 05 — 💬 User Query

A user submits a medical question through the Flask web interface.

### 06 — 🔎 Semantic Retrieval

The question is converted into an embedding and Pinecone retrieves the most relevant document chunks.

### 07 — 📚 Context Construction

The retrieved information is passed into the LangChain RAG pipeline as contextual information.

### 08 — 🤖 Gemini Generation

Google Gemini generates the final response based on the retrieved context and user question.

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Core programming language |
| 🔗 **LangChain** | RAG pipeline orchestration |
| 🤖 **Google Gemini** | Large Language Model |
| 🌲 **Pinecone** | Vector database and semantic search |
| 🤗 **Hugging Face** | Sentence-transformer embeddings |
| 🌐 **Flask** | Backend and web application |
| 📄 **PyPDF** | PDF document processing |
| 🔐 **python-dotenv** | Environment variable management |
| 🎨 **HTML/CSS** | User interface |
| 🐳 **Docker** | Application containerization |
| ☁️ **Fly.io** | Cloud deployment |

---

# 📂 Project Structure

    Medical-Chatbot/
    │
    ├── app.py
    ├── store_index.py
    ├── requirements.txt
    ├── setup.py
    ├── Dockerfile
    ├── fly.toml
    │
    ├── data/
    │   └── Medical PDFs
    │
    ├── src/
    │   ├── helper.py
    │   └── prompt.py
    │
    ├── static/
    │   ├── style.css
    │   └── Untitled-design.png
    │
    ├── templates/
    │   └── chat.html
    │
    └── README.md

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

    git clone https://github.com/al-foysal-tuhin/Medical-Chatbot.git

## 2️⃣ Enter the Project Directory

    cd Medical-Chatbot

## 3️⃣ Create a Virtual Environment

### Windows

    python -m venv venv

Activate the environment:

    venv\Scripts\activate

### Linux / macOS

    python3 -m venv venv
    source venv/bin/activate

## 4️⃣ Install Dependencies

    pip install -r requirements.txt

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

    GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
    PINECONE_API_KEY=YOUR_PINECONE_API_KEY

> 🔐 **Security:** Never commit your `.env` file or API keys to GitHub.

Your `.gitignore` should contain:

    .env
    venv/
    __pycache__/
    *.pyc

---

# 📚 Building the Vector Database

Place the medical PDF documents inside:

    data/

Then run:

    python store_index.py

This process:

1. Loads the medical PDF documents
2. Extracts the text
3. Splits the text into chunks
4. Generates embeddings
5. Stores the embeddings in Pinecone

Once the vector database has been created, the chatbot can use it for semantic retrieval.

---

# ▶️ Running the Application Locally

Start the Flask application:

    python app.py

The application will be available at:

    http://localhost:8080

Open the URL in your browser and ask a question.

### Example

    What is acne?

The application will:

    User Question
          ↓
    Semantic Search
          ↓
    Pinecone Retrieval
          ↓
    Relevant Medical Context
          ↓
    Gemini
          ↓
    Generated Answer

---

# ☁️ Deployment

The application is deployed using **Fly.io**.

### Production Application

🌐 **https://medical-chatbot-rag.fly.dev/**

The deployment uses environment variables for sensitive credentials, including:

    GOOGLE_API_KEY
    PINECONE_API_KEY

This prevents API credentials from being hard-coded into the application source code.

### Deployment Command

    fly deploy

### Check Deployment Status

    fly status

### View Application Logs

    fly logs --app medical-chatbot-rag

---

# ⚡ Deployment Characteristics

The production application currently runs as a containerized Flask application on Fly.io.

The deployed environment:

- 🐍 Python 3.10
- 🌐 Flask
- 🔗 LangChain
- 🤖 Google Gemini
- 🌲 Pinecone
- 🤗 Hugging Face embeddings
- 🐳 Docker
- ☁️ Fly.io

> ℹ️ The embedding model is loaded when the RAG pipeline is initialized. Because the model is relatively large, the first question after a cold start can take significantly longer than subsequent questions.

---

# 🧪 Example Interaction

### 👤 User

    What is a BUN test?

### 🔎 Behind the Scenes

    User Question
          ↓
    LangChain RAG Chain
          ↓
    Pinecone Similarity Search
          ↓
    Relevant Medical Documents
          ↓
    Retrieved Context
          ↓
    Google Gemini
          ↓
    Generated Medical Explanation

### 🤖 Result

The chatbot generates an answer using information retrieved from the medical knowledge base.

---

# 📊 Key Features

### 📄 Document Intelligence

Processes medical information from PDF documents and converts it into searchable knowledge.

### 🧠 Semantic Search

Uses vector embeddings instead of simple keyword matching to find contextually relevant information.

### 🌲 Pinecone Retrieval

Stores and retrieves document vectors efficiently using a vector database.

### 🤖 LLM Generation

Uses Google Gemini to transform retrieved context into natural-language responses.

### 🔗 LangChain Integration

Connects document retrieval, context processing, and language-model generation into a complete RAG workflow.

### 🌐 Web Application

Provides a simple Flask-based interface for interacting with the chatbot.

### ☁️ Cloud Deployment

The complete application is deployed and publicly accessible through Fly.io.

### 🔐 Secure Configuration

API credentials are handled through environment variables instead of being exposed in source code.

---

# 🔐 Security

This project uses environment variables for sensitive credentials.

API keys should never be hard-coded into Python files or committed to GitHub.

Example:

    GOOGLE_API_KEY=********
    PINECONE_API_KEY=********

If an API key is accidentally exposed:

1. Revoke the exposed key.
2. Generate a new key.
3. Update the environment variable.
4. Never commit the new key to the repository.

---

# ⚠️ Limitations

Although this project demonstrates a complete RAG workflow, it is still a learning and portfolio project.

Current limitations include:

- Responses depend on the quality of the retrieved documents.
- The chatbot may occasionally generate inaccurate information.
- The application does not replace professional medical advice.
- Cold starts can increase initial response time.
- The current application does not maintain persistent user conversation history.
- Retrieval quality can be further improved through reranking and evaluation.

---

# 🚀 Future Improvements

Possible future development includes:

- 👤 User authentication
- 💬 Persistent conversation history
- 🧠 Long-term conversational memory
- 📚 Source citations in responses
- 🔎 Retrieval reranking
- 🧪 Automated RAG evaluation
- 📊 Retrieval and response quality metrics
- 🎙️ Voice interaction
- 🌍 Multi-language support
- 🩺 Improved medical-domain prompting
- 📈 Application analytics
- 🐳 Docker Compose
- ☸️ Kubernetes deployment
- ⚡ Improved startup and model-loading performance
- 🛡️ Additional production security and monitoring

---

# 🎓 What I Learned From This Project

This project provided hands-on experience with:

- Retrieval-Augmented Generation
- Large Language Models
- Vector databases
- Semantic search
- Embedding models
- LangChain
- Google Gemini API
- Pinecone
- Flask
- REST-style application flow
- Environment variable management
- Docker
- Cloud deployment
- Production debugging
- Git and GitHub
- AI application architecture

---

# 🧩 Project Highlights

| Area | Implementation |
|---|---|
| **AI Architecture** | Retrieval-Augmented Generation |
| **LLM** | Google Gemini |
| **Embeddings** | Hugging Face Sentence Transformers |
| **Vector Database** | Pinecone |
| **Framework** | LangChain |
| **Backend** | Flask |
| **Documents** | Medical PDF knowledge base |
| **Containerization** | Docker |
| **Deployment** | Fly.io |
| **Version Control** | Git & GitHub |

---

# 👨‍💻 Author

## AL Foysal Tuhin

**Data Analyst • Data Science • AI/ML Enthusiast**

I am interested in building practical data and AI applications that combine machine learning, data engineering, and modern LLM technologies.

### 🔗 Connect With Me

**GitHub:**  
https://github.com/al-foysal-tuhin

**LinkedIn:**  
https://www.linkedin.com/in/alfoysaltuhin

---

# ⭐ Support

If you found this project interesting or useful, consider giving the repository a ⭐ on GitHub.

Your support helps the project become more visible and encourages further development.

---

# ⚠️ Medical Disclaimer

This project is an **educational and technical demonstration** of Retrieval-Augmented Generation, Large Language Models, vector databases, and AI application deployment.

The chatbot may produce inaccurate, incomplete, or inappropriate information.

**It must not be used for medical diagnosis, treatment decisions, emergency situations, or as a replacement for qualified medical professionals.**

Always consult an appropriate healthcare professional for medical concerns.

---

<p align="center">
  <strong>Built with 🧠 RAG + 🤖 Gemini + 🔗 LangChain + 🌲 Pinecone + 🌐 Flask</strong>
</p>

<p align="center">
  <strong>🚀 Deployed on Fly.io</strong>
</p>
---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Flask** | Web application framework |
| **LangChain** | RAG pipeline orchestration |
| **Google Gemini** | Large Language Model |
| **Pinecone** | Vector database |
| **Hugging Face** | Text embedding generation |
| **Sentence Transformers** | Semantic text embeddings |
| **PyPDF** | PDF document processing |
| **python-dotenv** | Environment variable management |
| **HTML/CSS** | Frontend |
| **Fly.io** | Cloud deployment |

---

## 📂 Project Structure

    Medical-Chatbot/
    │
    ├── app.py
    ├── store_index.py
    ├── requirements.txt
    ├── setup.py
    ├── Dockerfile
    ├── fly.toml
    │
    ├── data/
    │   └── Medical PDFs
    │
    ├── src/
    │   ├── helper.py
    │   └── prompt.py
    │
    ├── static/
    │   ├── style.css
    │   └── Untitled-design.png
    │
    ├── templates/
    │   └── chat.html
    │
    └── README.md

---

# ⚙️ Installation

## 1. Clone the Repository

    git clone https://github.com/al-foysal-tuhin/Medical-Chatbot.git

## 2. Move into the Project Directory

    cd Medical-Chatbot

## 3. Create a Virtual Environment

### Windows

    python -m venv venv

Activate it:

    venv\Scripts\activate

### Linux / macOS

    python -m venv venv
    source venv/bin/activate

## 4. Install Dependencies

    pip install -r requirements.txt

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

    GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
    PINECONE_API_KEY=YOUR_PINECONE_API_KEY

### Important

Never commit your `.env` file or API keys to GitHub.

Make sure `.env` is included in your `.gitignore`:

    .env
    venv/
    __pycache__/
    *.pyc

---

# 📚 Build the Vector Database

Place your medical PDF documents inside:

    data/

Then run:

    python store_index.py

The process will:

1. Load the PDF documents.
2. Extract the text.
3. Split the text into smaller chunks.
4. Generate vector embeddings.
5. Store the embeddings in Pinecone.

---

# ▶️ Run the Application Locally

Start the Flask application:

    python app.py

The application will run at:

    http://localhost:8080

Open the URL in your browser and start asking questions.

Example:

    What is acne?

The RAG pipeline retrieves relevant information from the medical knowledge base and sends the retrieved context to Gemini to generate the answer.

---

# ☁️ Deployment

The application is deployed using **Fly.io**.

### Production URL

    https://medical-chatbot-rag.fly.dev/

The deployment uses environment variables for sensitive credentials such as:

    GOOGLE_API_KEY
    PINECONE_API_KEY

This allows the application to run securely without exposing API credentials in the source code.

### Deployment Command

    fly deploy

The application runs inside a Docker container and listens on port `8080`.

---

# 🔄 RAG Workflow

The chatbot follows these main steps:

### 1. Document Loading

Medical information is loaded from PDF documents.

### 2. Text Splitting

Large documents are divided into smaller chunks so they can be efficiently searched.

### 3. Embedding Generation

Each text chunk is converted into a numerical vector using a Hugging Face Sentence Transformer model.

### 4. Vector Storage

The embeddings are stored in Pinecone.

### 5. User Query

The user submits a medical question through the Flask interface.

### 6. Semantic Retrieval

Pinecone searches for the most relevant document chunks.

### 7. Context + Question

The retrieved information is combined with the user's question.

### 8. Gemini Generation

Google Gemini generates the final response using the retrieved context.

---

# 🧪 Example

### User

    What is a BUN test?

### RAG Pipeline

    User Question
         ↓
    Pinecone Similarity Search
         ↓
    Relevant Medical Documents
         ↓
    LangChain Retriever
         ↓
    Retrieved Context
         ↓
    Google Gemini
         ↓
    Medical Explanation

The deployed application successfully processes questions through the complete RAG pipeline, including embedding loading, Pinecone retrieval, and Gemini response generation.

---

# 📦 Main Python Libraries

    langchain
    langchain-core
    langchain-community
    langchain-pinecone
    langchain-google-genai
    langchain-huggingface
    google-genai
    flask
    sentence-transformers
    pypdf
    python-dotenv

Exact versions are maintained in:

    requirements.txt

---

# 🔐 Security

API credentials are stored using environment variables rather than being hard-coded into the application.

Sensitive credentials should **never** be committed to GitHub.

Example:

    GOOGLE_API_KEY=********
    PINECONE_API_KEY=********

For local development, use a `.env` file.

For production deployment, configure secrets through the deployment platform rather than storing them in the repository.

---

# 🚀 Future Improvements

Some planned improvements include:

- 👤 User authentication
- 💬 Conversation history
- 🧠 Persistent chat memory
- 🎙️ Voice-based interaction
- 📚 Medical source citations
- 🩺 Improved medical-domain prompting
- 🔎 Improved retrieval and reranking
- 📊 RAG evaluation and performance metrics
- 🧪 Automated evaluation of RAG responses
- 🐳 Improved containerization and production deployment
- ☸️ Kubernetes deployment

---

# 👨‍💻 Author

**AL Foysal Tuhin**

### GitHub

https://github.com/al-foysal-tuhin

### LinkedIn

https://www.linkedin.com/in/alfoysaltuhin

---

# ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

It helps support the project and makes it easier for others to discover.

---

## ⚠️ Medical Disclaimer

This application is an educational demonstration of Retrieval-Augmented Generation and Large Language Models.

The responses generated by the chatbot may contain inaccuracies and should **not** be considered professional medical advice, diagnosis, or treatment recommendations.

Always consult a qualified healthcare professional for medical concerns.
