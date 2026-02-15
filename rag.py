import ollama
import chromadb
from chromadb.config import Settings
import os

print("Starting RAG...")

# Create persistent DB
client = chromadb.Client(Settings(persist_directory="./db"))

collection = client.get_or_create_collection(name="rag_collection")

# Load data ONLY if empty
if collection.count() == 0:

    print("Storing documents...")

    with open("data.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # Split into chunks (VERY IMPORTANT)
    chunks = text.split("\n\n")

    for i, chunk in enumerate(chunks):

        if chunk.strip() == "":
            continue

        embedding = ollama.embeddings(
            model="nomic-embed-text",
            prompt=chunk
        )["embedding"]

        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[chunk]
        )

    print("Stored successfully!")

else:
    print("DB already exists")

print("RAG Ready")

# Query loop
while True:

    query = input("\nAsk question: ")

    if query.lower() == "exit":
        break

    query_embedding = ollama.embeddings(
        model="nomic-embed-text",
        prompt=query
    )["embedding"]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    context = "\n".join(results["documents"][0])

    prompt = f"""
You are an assistant. Answer ONLY using the context below.

Context:
{context}

Question:
{query}

Answer:
"""

    response = ollama.chat(
        model="gemma3:1b",
        messages=[{"role": "user", "content": prompt}]
    )

    print("\nAnswer:")
    print(response["message"]["content"])
