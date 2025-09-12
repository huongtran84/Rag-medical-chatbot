import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
HF_TOKEN = os.environ.get("HF_TOKEN")
HUGGINGFACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"
DB_FAISS_PATH = "vectorstore/faiss_db"
DATA_PATH = "data/"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50