from Libraries.lib import Pinecone
from src.helpers.logger import logger
from src.helpers.config import (
    PINECONE_API_KEY, 
    INDEX_NAME, 
    NAMESPACE
)

def clear_pinecone_namespace():
    pc = Pinecone(api_key=PINECONE_API_KEY)
    idx = pc.Index(INDEX_NAME)

    try:
        idx.delete(delete_all=True, namespace=NAMESPACE)
        logger.info(f"🗑️ Cleared all data from namespace: {NAMESPACE}")
    except Exception as e:
        logger.error(f"❌ Error clearing namespace: {e}")
        raise
