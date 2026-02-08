#!/usr/bin/env python3
"""
RAG System - Question Answering from FAQ

This script provides a command-line interface to query a RAG system
that answers questions based on indexed FAQ data.
"""
from Libraries.lib import os, sys, Path

# Add the project root to the Python path
sys.path.append(str(Path(__file__).parent))

from services.generator import generate_answer
from services.pinecone_service import load_and_index_data
from src.helpers.config import FAQ_CSV_PATH

def print_banner():
    """Print the application banner."""
    banner = """
    ╔══════════════════════════════════════════╗
    ║           FAQ RAG System                 ║
    ║  Ask questions about the indexed FAQ     ║
    ║  Type 'exit' or 'quit' to end the session ║
    ╚══════════════════════════════════════════╝
    """
    print(banner)

def main():
    """Main function to run the RAG system."""
    # Check if data needs to be indexed
    if not FAQ_CSV_PATH.exists():
        print(f"Error: Could not find FAQ CSV file at {FAQ_CSV_PATH}")
        print("Please ensure the file exists and try again.")
        return
        
    print("Checking Pinecone index...")
    if not load_and_index_data():
        print("Failed to initialize Pinecone index. Please check your configuration.")
        return
    
    print("\nRAG System is ready!")
    print("Enter your questions below. Type 'exit' or 'quit' to end the session.")
    print("-" * 50)
    
    # Main interaction loop
    while True:
        try:
            # Get user input
            query = input("\nYour question: ").strip()
            
            # Check for exit command
            if query.lower() in ('exit', 'quit'):
                print("\nThank you for using the FAQ RAG System. Goodbye!")
                break
                
            if not query:
                print("Please enter a question or type 'exit' to quit.")
                continue
                
            # Generate and display answer
            print("\nSearching for answers...")
            answer = generate_answer(query)
            print("\n" + "=" * 50)
            print(f"Question: {query}")
            print("-" * 50)
            print(f"Answer: {answer}")
            print("=" * 50)
            
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            print("Please try again or type 'exit' to quit.")

if __name__ == "__main__":
    print_banner()
    main()
