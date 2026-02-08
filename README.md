# FAQ RAG System

A sophisticated Retrieval-Augmented Generation (RAG) system designed to provide accurate answers from FAQ data using semantic search and large language models. This system leverages **Pinecone** for vector database management and **Google Gemini** for high-quality response generation.

## 🚀 Features

- **Semantic Search**: Uses Pinecone's integrated embedding models to find relevant answers even when keywords don't match exactly.
- **Context-Aware Generation**: Employs Google's Gemini models to synthesize helpful, human-like answers strictly based on retrieved context.
- **Dynamic Indexing**: Automatically checks and indexes CSV data into Pinecone upon startup.
- **Extensible Architecture**: Cleanly separated services for indexing, retrieval, and generation.
- **CLI Interface**: Easy-to-use command-line interface for interactive querying.

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Vector Database**: [Pinecone](https://www.pinecone.io/)
- **LLM**: [Google Gemini](https://ai.google.dev/)
- **Data Handling**: Pandas
- **Environment Management**: Python-dotenv

## 📁 Project Structure

```text
RAG_System/
├── main.py                 # Entry point: CLI interface
├── services/
│   ├── pinecone_service.py # Indexing and index management
│   ├── retrieval.py        # Semantic search logic
│   └── generator.py        # LLM response generation
├── src/
│   ├── helpers/
│   │   ├── config.py       # Configuration and environment loading
│   │   ├── logger.py       # Centralized logging
│   │   └── prompt.py       # System instructions for the LLM
│   └── data/               # Data directory
│       └── cleaned_faq.csv # Source FAQ dataset
├── requirements.txt        # Project dependencies
└── .env                    # API keys (not in version control)
```

## ⚙️ Setup Instructions

### 1. Prerequisites
- Python 3.10 or higher
- A Pinecone API Key
- A Google AI (Gemini) API Key

### 2. Installation
Clone the repository and install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the project root and add your API keys:
```env
PINECONE_API_KEY="your_pinecone_key"
GEMINI_API_KEYS="your_gemini_key"
```

You can customize the index name, region, and model in `src/helpers/config.py`.

## 🎮 How to Run

Execute the main script to start the interactive CLI:
```bash
python main.py
```

### Initial indexing
On the first run, the system will:
1. Initialize or connect to your Pinecone index.
2. Load data from `src/data/cleaned_faq.csv`.
3. Generate embeddings and upsert them into Pinecone.

## 🔍 Key Components

### **Indexing Service** (`services/pinecone_service.py`)
Handles the connection to Pinecone. It uses the `create_index_for_model` feature, which integrates embedding generation directly into the Pinecone platform (using `text-embedding-3-large`).

### **Retrieval Service** (`services/retrieval.py`)
Performs semantic search against the Pinecone index. It is configured to return the top 10 most relevant matches to provide rich context to the LLM.

### **Generation Service** (`services/generator.py`)
Constructs a prompt containing the retrieved FAQ snippets and the user query. It uses `gemini-flash-latest` to generate a concise and factual response.

### **Prompting** (`src/helpers/prompt.py`)
Contains the "personality" and rules for the AI, ensuring it stays grounded in the provided CSV data and handles "I don't know" cases gracefully.

---
*Created as part of a Self Learning Journey.*
