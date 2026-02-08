"""Module for retrieving relevant documents from Pinecone."""
from Libraries.lib import Pinecone, SearchQuery
from src.helpers.config import PINECONE_API_KEY, INDEX_NAME, NAMESPACE
from src.helpers.logger import logger

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)
idx = pc.Index(INDEX_NAME)

def retrieve_relevant_documents(query, top_k=10):
    """Retrieve relevant documents from Pinecone based on the query.
    
    Args:
        query (str): The user's query
        top_k (int): Number of results to return
        
    Returns:
        dict: Search results from Pinecone
    """
    try:
        response = idx.search_records(
            namespace=NAMESPACE,
            query=SearchQuery(
                inputs={"text": query},
                top_k=top_k,
            )
        )
        return response
    except Exception as e:
        logger.error(f"Error retrieving documents: {e}")
        return {"result": {"hits": []}}
