# Discord-Rag-Chatbot
RAG FAQ Bot: Discord + Web Interface

Welcome to the RAG FAQ Bot — a Retrieval-Augmented Generation (RAG) powered assistant that works both as a Discord bot and a Gradio web app. This bot allows users to ask natural language questions based on an internal FAQ PDF.

🚀 Live Links

🌐 Web App (Gradio): https://huggingface.co/spaces/CMB040/rag-faq-bot

🤖 Discord Bot Server: https://discord.gg/U5mczbRc

🔎 Features

📄 Ingests PDF documents (FAQ-style)

🔍 Semantic search using vector similarity (FAISS)

🧠 Embeddings powered by Hugging Face models

🤖 Available as both CLI, Web App, and Discord Bot

🔊 Voice-compatible with text input/output

🧰 Tech Stack & Libraries

🧠 LLMs and Models

sentence-transformers/all-MiniLM-L6-v2 via Hugging Face

LangChain (with RAG chaining logic)

FAISS (for fast vector search)

🛠️ Python Libraries

langchain, langchain_community, langchain_huggingface

gradio (for web UI)

discord.py (for bot integration)

dotenv (environment handling)

PyMuPDF (PDF loader)

📁 Project Structure

rag-discord-bot/
├── .env                         # API keys (Discord, HF Token) [DO NOT COMMIT]
├── ingest.py                   # Script to convert PDF → Vector DB
├── rag_query.py                # CLI test script
├── rag_web.py                  # Web-based chatbot
├── discord_bot.py              # Discord bot version
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
├── data/
│   └── faq.pdf, datafaq.pdf    # Your documents
├── requirements.txt            # All dependencies

🔐 .env Format

HUGGINGFACEHUB_API_TOKEN=hf_...
DISCORD_TOKEN=your_discord_token_here

✅ Ensure .env is included in .gitignore to avoid leaking secrets.

🔧 Setup Instructions

# Clone the project
$ git clone https://github.com/yourname/project_rag_bot.git
$ cd project_rag_bot

# Create virtual environment
$ python -m venv .venv
$ source .venv/Scripts/activate  # Windows

# Install dependencies
$ pip install -r requirements.txt

# Ingest PDF data
$ python ingest.py

# Launch Web Interface
$ python rag_web.py

# Run Discord Bot
$ python discord_bot.py

💻 Optional: Azure Deployment

Want Me to Prepare a .zip Ready for Azure?
Just say “yes” — I’ll package your code for easy uploading.

🚀 Summary

Step

Status

Create Azure account

✅ Done

Create VM

🛠️ You Do

Upload bot code

🔼 Easy

Install Python & deps

🧪 Yes

Run bot 24/7

✅ With screen

Done 🎉

🟢 Ready

Let me know when your VM is up — I’ll help live.

📄 License

This project is for educational/demo use. Please do not upload API keys publicly.

🙋‍♂️ Author

CMB040  — built as part of AI/ML intern project to demonstrate LLM integration with real-time assistants.

