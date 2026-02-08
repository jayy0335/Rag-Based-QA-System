"""Module for generating responses using the Gemini model."""
from Libraries.lib import genai, GenerateContentConfig, Part
from src.helpers.config import GEMINI_API_KEY
from .retrieval import retrieve_relevant_documents
from src.helpers.prompt import prompt as system_prompt
from src.helpers.logger import logger

def generate_answer(query):
    """Generate an answer to the user's query using retrieved context.
    
    Args:
        query (str): The user's question
        
    Returns:
        str: Generated answer
    """
    try:
        # Retrieve relevant documents
        matches = retrieve_relevant_documents(query)
        
        retrieved_chunks = []
        for i, hit in enumerate(matches['result']['hits'], 1):
            retrieved_chunks.append(f"[FAQ {i}]\n{hit['fields']['chunk_text']}")

        
        context = "\n\n---\n\n".join(retrieved_chunks)

        
        if not context:
            return "I couldn't find any relevant information to answer your question."
            
        # Initialize Gemini client
        client = genai.Client(api_key=GEMINI_API_KEY)
        model = 'gemini-flash-latest'
        
        # Create prompt with context and query
        prompt = f"""
            SYSTEM INSTRUCTIONS:
            {system_prompt}

            CSV CONTEXT (retrieved rows):
            {context}

            USER QUESTION:
            {query}

            Answer using only the CSV context above.
        """
        
        # Generate response
        response = client.models.generate_content(
            model=model,
            contents=[Part.from_text(text=prompt)],
            config=GenerateContentConfig(
                temperature=0.1 ,  # more factual
                top_p=0.95,
                top_k=50,
            ),
        )
        return response.text
        
    except Exception as e:
        logger.error(f"Error generating answer: {e}")
        return "I'm sorry, I encountered an error while processing your request."
