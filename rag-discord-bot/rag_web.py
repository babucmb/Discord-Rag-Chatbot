import gradio as gr
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

retriever = FAISS.load_local(
    "vectorstore",
    HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),
    allow_dangerous_deserialization=True
).as_retriever()

qa_model = pipeline("text2text-generation", model="google/flan-t5-base")

def ask_question(query):
    docs = retriever.get_relevant_documents(query, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    prompt = f"Answer the question based on the context below:\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"
    result = qa_model(prompt, max_length=300, do_sample=False)[0]['generated_text']
    return result

iface = gr.Interface(fn=ask_question, inputs="text", outputs="text", title="RAG FAQ Chatbot")
iface.launch(share=True)
