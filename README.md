# RAG Project using Ollama and ChromaDB

This project implements a simple Retrieval-Augmented Generation (RAG) system using Ollama, ChromaDB, and Python. The system allows you to ask questions and receive answers based on your own custom data stored in a text file. It works completely locally without requiring any cloud services.

------------------------------------------------------------

## Features

• Fully local RAG system (no internet required after setup)  
• Uses Ollama gemma3:1b model for answer generation  
• Uses nomic-embed-text model for embeddings  
• Uses ChromaDB as vector database  
• Persistent storage of embeddings  
• Fast semantic search  
• Simple terminal-based chatbot  
• Easy to customize with your own data  

------------------------------------------------------------

## Technologies Used

Python  
Ollama  
ChromaDB  
Embedding Model: nomic-embed-text  
LLM Model: gemma3:1b  

------------------------------------------------------------

## Project Structure

rag/
│
├── rag.py        → Main RAG application  
├── data.txt      → Knowledge base file  
├── README.md     → Project documentation  
├── db/           → Vector database (auto-created)  

------------------------------------------------------------

## Installation

Step 1: Install Python libraries

pip install ollama chromadb

Step 2: Install Ollama

Download from: https://ollama.com/download

Step 3: Pull required models

ollama pull gemma3:1b  
ollama pull nomic-embed-text  

------------------------------------------------------------

## Running the Project

Step 1: Start Ollama server

ollama serve

Step 2: Run the RAG application

python rag.py

------------------------------------------------------------

## Example Usage

Ask question:

What is my name?

Output:

Your name is Nandhagopal V.

------------------------------------------------------------

## How It Works

1. Loads data from data.txt  
2. Splits text into chunks  
3. Converts chunks into embeddings  
4. Stores embeddings in ChromaDB  
5. Converts user question into embedding  
6. Finds most relevant chunks  
7. Sends context to gemma3 model  
8. Generates accurate answer  

------------------------------------------------------------

## Use Cases

Personal AI assistant  
Document question answering  
Interview preparation chatbot  
Knowledge-based chatbot  
Offline AI assistant  

------------------------------------------------------------

## Author

Nandhagopal V  

GitHub: https://github.com/nandhu-boy  

------------------------------------------------------------

## Future Improvements

Add PDF support  
Add web interface  
Add chat history  
Improve UI  
Add multiple document support  

------------------------------------------------------------

## License

This project is open source and free to use.
