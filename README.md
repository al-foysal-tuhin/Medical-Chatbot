# 🩺 Medical Chatbot using LangChain, Pinecone, Gemini & Flask

A Retrieval-Augmented Generation (RAG) based Medical Chatbot that answers medical questions using a knowledge base built from PDF documents.

The application uses Google's Gemini model for text generation, Pinecone as the vector database, LangChain for orchestration, and Flask for the web interface.

---

## 🚀 Features

- 📄 PDF document ingestion
- ✂️ Automatic text chunking
- 🔍 Semantic search using Pinecone
- 🤖 Google Gemini integration
- ⚡ Retrieval-Augmented Generation (RAG)
- 🌐 Flask web interface
- ☁️ Ready for cloud deployment (Render)

---

## 🛠 Tech Stack

- Python
- Flask
- LangChain
- Google Gemini API
- Pinecone Vector Database
- Hugging Face Sentence Transformers
- PyPDF
- HTML/CSS
- Render

---

## 📂 Project Structure

```
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

Clone the repository

```bash
git clone https://github.com/al-foysal-tuhin/Medical-Chatbot.git
```

Move into the project

```bash
cd Medical-Chatbot
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
PINECONE_API_KEY=YOUR_PINECONE_API_KEY
```

---

# 📚 Build the Vector Database

Place your PDF files inside

```
data/
```

Then run

```bash
python store_index.py
```

This will

- Load PDFs
- Split documents into chunks
- Generate embeddings
- Upload vectors to Pinecone

---

# ▶️ Run the Application

```bash
python app.py
```

The application will be available at

```
http://localhost:8080
```

---

# 🌐 Deployment

This project can be deployed on cloud platforms such as

- Render
- AWS EC2
- Railway
- Fly.io
- Azure App Service

---

# 📷 Application Workflow

```
PDF Documents
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
      │
      ▼
Embedding Model
      │
      ▼
Pinecone Vector Database
      │
      ▼
Retriever
      │
      ▼
Google Gemini
      │
      ▼
Medical Response
```

---

# 📦 Main Libraries

- Flask
- LangChain
- LangChain Pinecone
- LangChain Google GenAI
- Sentence Transformers
- Pinecone
- PyPDF
- Python Dotenv

---

# 💡 Future Improvements

- User authentication
- Chat history
- Conversation memory
- Voice assistant
- Medical source citations
- Docker Compose
- Kubernetes deployment

---

# 👨‍💻 Author

**AL Foysal Tuhin**

- GitHub: https://github.com/al-foysal-tuhin
- LinkedIn: www.linkedin.com/in/alfoysaltuhin

---

# ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future development.
