import os
from dotenv import load_dotenv
from chromadb.config import Settings

load_dotenv()

# Define the folder for storing database



PERSIST_DIRECTORY="db"
MODEL_TYPE="LlamaCpp"
#MODEL_PATH=/content/privateGPT/models/nous-hermes-llama2-13b.ggmlv3.q4_1.bin
MODEL_PATH="/content/privateGPT/models/nous-hermes-llama2-13b.Q2_K.gguf"
EMBEDDINGS_MODEL_NAME="all-MiniLM-L6-v2"
MODEL_N_CTX=1000
MODEL_N_BATCH=8
TARGET_SOURCE_CHUNKS=4
SOURCE_DIRECTORY = "/content/privateGPT/source_documents"

# Define the Chroma settings
CHROMA_SETTINGS = Settings(
        chroma_db_impl='duckdb+parquet',
        persist_directory=PERSIST_DIRECTORY,
        anonymized_telemetry=False
)
