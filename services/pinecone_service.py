from Libraries.lib import pd, Pinecone
from src.helpers.logger import logger
from src.helpers.config import (
    PINECONE_API_KEY, 
    INDEX_NAME, 
    CLOUD, 
    REGION, 
    EMBED_MODEL, 
    NAMESPACE,
    FAQ_CSV_PATH
)


def initialize_pinecone_index():
    """Initialize or connect to the Pinecone index."""
    pc = Pinecone(api_key=PINECONE_API_KEY)
    
    try:
        # First try to get the index
        return pc.Index(INDEX_NAME)
    except Exception:
        # If index doesn't exist, create it
        try:
            pc.create_index_for_model(
        name=INDEX_NAME,
        cloud=CLOUD,
        region=REGION,
        embed={
            "model": EMBED_MODEL,
            "field_map": {"text": "chunk_text"}
        }
    )
            logger.info(f"✅ Successfully created Pinecone index: {INDEX_NAME}")
            return pc.Index(INDEX_NAME)
        except Exception as e:
            logger.error(f"Error creating Pinecone index: {e}")
            raise

def load_and_index_data():
    """Load data from CSV and index it in Pinecone."""
    try:
        # Initialize Pinecone index
        idx = initialize_pinecone_index()
        
        # Load the CSV file
        if not FAQ_CSV_PATH.exists():
            logger.error(f"Error: Could not find CSV file at {FAQ_CSV_PATH}")
            return False
            
        df = pd.read_csv(FAQ_CSV_PATH)
        
        # Prepare records for indexing
        records = []
        for i, row in df.iterrows():
            question = str(row["questions"])  # adjust column names as per your CSV
            answer = str(row["answers"])      # adjust column names as per your CSV
            combined_text = (
                f"FAQ Question: {question} | "
                f"FAQ Answer: {answer} | "
                f"Type: FAQ | "
                f"Source: CSV"
            )

            records.append({
                "_id": f"faq_{i}",
                "chunk_text": combined_text,
                "question": question,
                "answer": answer
            })

        
        # Upsert records in chunks
        chunk_size = 50
        for i in range(0, len(records), chunk_size):
            chunk = records[i:i+chunk_size]
            idx.upsert_records(namespace=NAMESPACE, records=chunk)
        
        logger.info(f"✅ Successfully indexed {len(records)} FAQ entries in Pinecone.")
        return True
        
    except Exception as e:
        logger.error(f"❌ Error during data indexing: {str(e)}")
        return False
