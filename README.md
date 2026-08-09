# 🩺 Medical Chatbot using LangChain, Pinecone, Gemini & Flask

An AI-powered **Retrieval-Augmented Generation (RAG) Medical Chatbot** that answers medical questions using information retrieved from a medical knowledge base built from PDF documents.

The application combines **LangChain**, **Google Gemini**, **Pinecone Vector Database**, **Hugging Face Sentence Transformers**, and **Flask** to build an end-to-end RAG pipeline and deploy it as a web application.

## 🚀 Live Demo

### 🌐 Try the Medical Chatbot

👉 **https://medical-chatbot-rag.fly.dev/**

> ⏳ **Note:** Because the application is hosted on Fly.io, the first request after a period of inactivity may take a little longer while the server wakes up and loads the embedding model and RAG pipeline. Subsequent requests should respond much faster.

> ⚠️ **Medical Disclaimer:** This chatbot is intended for educational and informational purposes only. It does not provide medical diagnosis or replace advice from a qualified healthcare professional.

---

## ✨ Features

* 📄 PDF document ingestion
* ✂️ Automatic document text splitting and chunking
* 🧠 Hugging Face sentence-transformer embeddings
* 🔍 Semantic similarity search
* 🗄️ Pinecone vector database
* 🤖 Google Gemini 3.5 Flash for response generation
* 🔗 LangChain RAG pipeline
* 🌐 Flask web interface
* ☁️ Cloud deployment with Fly.io
* 🔐 Environment-variable based API key management

---

## 🏗️ Architecture

The chatbot follows a Retrieval-Augmented Generation architecture:

```text
                 Medical PDF Documents
                          │
                          ▼
                  Document Loader
                          │
                          ▼
                   Text Splitter
                          │
                          ▼
              Hugging Face Embeddings
                          │
                          ▼
                Pinecone Vector DB
                          │
                          ▼
                      Retriever
                          │
                    User Question
                          │
                          ▼
                Relevant Documents
                          │
                          ▼
                 Google Gemini 3.5
                          │
                          ▼
                  Generated Answer
                          │
                          ▼
                    Flask Web UI
```

---

## 🛠️ Tech Stack

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| **Python**        | Core programming language       |
| **Flask**         | Web application framework       |
| **LangChain**     | RAG pipeline orchestration      |
| **Google Gemini** | Large Language Model            |
| **Pinecone**      | Vector database                 |
| **Hugging Face**  | Text embeddings                 |
| **PyPDF**         | PDF document processing         |
| **python-dotenv** | Environment variable management |
| **HTML/CSS**      | Frontend                        |
| **Fly.io**        | Cloud deployment                |

---

## 📂 Project Structure

```text
Medical-Chatbot/
│
├── app.py
├── store_index.py
├── requirements.txt
├── setup.py
├── Dockerfile
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
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/al-foysal-tuhin/Medical-Chatbot.git
```

## 2. Move into the Project Directory

```bash
cd Medical-Chatbot
```

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PINECONE_API_KEY=YOUR_PINECONE_API_KEY
```

### Important

Never commit your `.env` file or API keys to GitHub.

Make sure `.env` is included in your `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

# 📚 Build the Vector Database

Place your medical PDF documents inside:

```text
data/
```

Then run:

```bash
python store_index.py
```

The process will:

1. Load the PDF documents.
2. Extract the text.
3. Split the text into smaller chunks.
4. Generate vector embeddings.
5. Store the embeddings in Pinecone.

---

# ▶️ Run the Application Locally

Start the Flask application:

```bash
python app.py
```

The application will run at:

```text
http://localhost:8080
```

Open the URL in your browser and start asking questions.

Example:

```text
What is acne?
```

The RAG pipeline retrieves relevant information from the medical knowledge base and sends the context to Gemini to generate the answer.

---

# ☁️ Deployment

The application is deployed using **Fly.io**.

### Production URL

```text
https://medical-chatbot-rag.fly.dev/
```

The deployment uses environment variables for sensitive credentials such as:

```text
GOOGLE_API_KEY
PINECONE_API_KEY
```

This allows the application to run securely without exposing API credentials in the source code.

---

# 🔄 RAG Workflow

The chatbot follows these main steps:

### 1. Document Loading

Medical information is loaded from PDF documents.

### 2. Text Splitting

Large documents are divided into smaller chunks so they can be efficiently searched.

### 3. Embedding Generation

Each text chunk is converted into a numerical vector using a Hugging Face embedding model.

### 4. Vector Storage

The embeddings are stored in Pinecone.

### 5. User Query

The user submits a medical question through the Flask interface.

### 6. Semantic Retrieval

Pinecone searches for the most relevant document chunks.

### 7. Context + Question

The retrieved information is combined with the user's question.

### 8. Gemini Generation

Google Gemini 3.5 Flash generates the final response using the retrieved context.

---

# 🧪 Example

### User

```text
What is acne?
```

### RAG Pipeline

```text
User Question
     ↓
Pinecone Similarity Search
     ↓
Relevant Medical Documents
     ↓
LangChain Retriever
     ↓
Gemini 3.5 Flash
     ↓
Medical Explanation
```

---

# 📦 Main Python Libraries

```text
Flask
LangChain
LangChain Pinecone
LangChain Google GenAI
Google GenAI
Sentence Transformers
Pinecone
PyPDF
Python Dotenv
```

---

# 🔐 Security

API credentials are stored using environment variables rather than being hard-coded into the application.

Sensitive credentials should **never** be committed to GitHub.

Example:

```env
GOOGLE_API_KEY=********
PINECONE_API_KEY=********
```

---

# 🚀 Future Improvements

Some planned improvements include:

* 👤 User authentication
* 💬 Conversation history
* 🧠 Persistent chat memory
* 🎙️ Voice-based interaction
* 📚 Medical source citations
* 🩺 Improved medical-domain prompting
* 🐳 Docker Compose
* ☸️ Kubernetes deployment
* 📊 User analytics
* 🔎 Improved retrieval and reranking
* 🧪 Automated evaluation of RAG responses

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

