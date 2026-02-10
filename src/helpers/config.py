"""Configuration settings for the RAG system."""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).parent.parent

# API Keys
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEYS")

# Pinecone Configuration
INDEX_NAME = "developer-quickstart-py"
CLOUD = "aws"
REGION = "us-east-1"
EMBED_MODEL = "text-embedding-3-large"
NAMESPACE = "faq"

# File Paths
DATA_DIR = BASE_DIR / "data"
FAQ_CSV_PATH = DATA_DIR / "faqs.csv"

# Ensure data directory exists
DATA_DIR.mkdir(parents=True, exist_ok=True)
