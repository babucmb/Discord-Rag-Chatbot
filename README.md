# 🤖 RAG FAQ Bot (Discord + Web)

A Retrieval-Augmented Generation (RAG) bot that answers questions from a PDF FAQ document using **Hugging Face models**. This bot is available via both **Gradio Web UI** and a **Discord Bot**.

---

## 🔗 Live Links

- 🌐 Web App (Gradio): [https://4d261da699ca0b7580.gradio.live](https://huggingface.co/spaces/CMB040/rag-faq-bot))
- 💬 Discord Bot Server: [Join Discord Server](https://discord.gg/U5mczbRc))

---

## 📌 Features

- Upload a PDF and ask questions about its content
- Supports both **Web** and **Discord** interfaces
- Powered by **Hugging Face Embeddings**
- Uses **FAISS** for vector storage & fast retrieval
- Fully customizable with LangChain modules

---

## 🧠 Technologies Used

### Libraries
- `langchain`
- `langchain_community`
- `langchain_huggingface`
- `transformers`
- `discord.py`
- `gradio`
- `python-dotenv`
- `PyMuPDF` (PDF parsing)
- `faiss-cpu`

### Models
- `sentence-transformers/all-MiniLM-L6-v2` (for embeddings)

---

## 📁 Project Structure

rag-discord-bot/
├── .env # Environment variables (API keys)
├── data/
│ └── faq.pdf # Input document
├── ingest.py # PDF → Chunk → Embeddings → FAISS
├── rag_query.py # Local CLI interface
├── rag_web.py # Gradio Web Interface
├── discord_bot.py # Discord Bot handler
├── vectorstore/
│ ├── index.faiss
│ └── index.pkl
├── requirements.txt

yaml
Copy
Edit

---

## 🔐 .env File Format

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
DISCORD_TOKEN=your_discord_bot_token
⚠️ Important: Never push .env to GitHub! Add it to .gitignore.

⚙️ Setup Instructions
1. Clone & Create Virtual Environment
bash
Copy
Edit
git clone https://github.com/your-username/rag-discord-bot.git
cd rag-discord-bot

python -m venv .venv
.\.venv\Scripts\activate  # Windows
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Ingest Document
bash
Copy
Edit
python ingest.py
4. Test Locally (CLI)
bash
Copy
Edit
python rag_query.py
5. Launch Web App
bash
Copy
Edit
python rag_web.py
6. Start Discord Bot
bash
Copy
Edit
python discord_bot.py
☁️ Deployment Notes
Hosting 24/7
You can deploy this on:

Hugging Face Spaces (Web Only)

Railway.app

Render.com

Azure VM (for full Discord/Web stack)

🛠 Recommended Tools
Use .gitignore to exclude .env and vectorstore/

For Discord bot hosting, use a VM or service that supports persistent Python background tasks

Use screen or tmux if deploying on Azure/Linux VM

👨‍💻 Author
Built by Chilakani Mahesh Babu (CMB040)
As part of an AI project to demonstrate LLM + RAG deployment in multiple interfaces.

📜 License
This project is open-source and intended for educational purposes only. Do not push API keys or private PDFs to any public repository.

yaml
Copy
Edit

---

Let me know if you'd like to:
- Add badges (like `Python`, `LangChain`, `HuggingFace`, etc.)
- Auto-generate a GitHub Pages documentation
- Add deployment steps for Railway or Azure VM

Ready to copy-paste into your `README.md`!
