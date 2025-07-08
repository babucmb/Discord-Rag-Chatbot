from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()

retriever = FAISS.load_local(
    "vectorstore",
    HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),
    allow_dangerous_deserialization=True
).as_retriever()


qa_model = pipeline("text2text-generation", model="google/flan-t5-base")

def ask_question(query):
    docs = retriever.get_relevant_documents(query)
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"Answer the question based on the context below:\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"

    result = qa_model(prompt, max_length=300, do_sample=False)[0]['generated_text']
    return result

if __name__ == "__main__":
    while True:
        query = input("\nAsk your question (or type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        answer = ask_question(query)
        print("\nAnswer:", answer)
