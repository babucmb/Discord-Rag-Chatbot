import discord
from discord.ext import commands
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

retriever = FAISS.load_local(
    "vectorstore",
    HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),
    allow_dangerous_deserialization=True
).as_retriever()

qa_model = pipeline("text2text-generation", model="google/flan-t5-base")

def ask_rag(query):
    docs = retriever.get_relevant_documents(query)
    context = "\n".join([doc.page_content for doc in docs])
    prompt = f"Answer the question based on the context:\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"
    result = qa_model(prompt, max_length=300, do_sample=False)[0]['generated_text']
    return result

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    query = message.content
    response = ask_rag(query)
    await message.channel.send(response)

bot.run(TOKEN)
