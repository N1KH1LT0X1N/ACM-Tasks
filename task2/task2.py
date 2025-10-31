"""
AI PDF Summarizer Module

This module provides functionality to extract text from PDFs and generate
AI-powered summaries using the Groq API with Llama 3.3 70B model.

Features:
- Text extraction from text-based PDFs
- AI-powered summarization with customizable length and style
- Robust error handling for various PDF types
- Environment-based API key management

Author: Nikhil Toxin
Created for: DJSCE ACM Research Club Technical Interview 2025
"""

import os
import sys
from dotenv import load_dotenv
import pdfplumber
from langchain_groq.chat_models import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set. Please add it to your .env file.")

llm = ChatGroq(model_name="llama-3.3-70b-versatile")

def extract_text_from_pdf(pdf_file):
    """
    Extracts clean text from a text-based PDF while handling edge cases.
    
    Args:
        pdf_file (str): Path to the PDF file
        
    Returns:
        str: Extracted text or error message
        
    Note:
        Returns a warning message if PDF contains no readable text
        (e.g., scanned or image-based PDFs)
    """
    """Extracts clean text from a text-based PDF while handling edge cases."""
    text = ""
    try:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text.strip() + "\n\n" 
    except Exception as e:
        return f"Error extracting text: {str(e)}"

    if not text.strip():
        return "⚠️ No readable text found. This might be a scanned or image-based PDF."

    return text.strip()

def summarize_text(text, length, style):
    """
    Summarizes extracted text with structured formatting using AI.
    
    Args:
        text (str): Text to summarize
        length (str): Desired length ("brief", "detailed", etc.)
        style (str): Output format ("bullet points", "paragraph", etc.)
        
    Returns:
        str: AI-generated summary
        
    Note:
        Limits input to 10,000 characters for efficiency
    """
    prompt = (
        f"""
        Read the following document and extract unstructured information and convert it into a structured summary in {style.lower()} format.
        Keep the information {length.lower()}.
        Follow this structured reasoning:
        1. Extract useful information from the document.
        2. Make unstructured information structured.
        3. Remove redundant information.
        4. Ensure accuracy without hallucination.
        Document:
        {text[:10000]}  # Limit input to 10,000 characters for efficiency

        """
    )
    response = llm.predict(prompt)
    return response.strip()

def process_pdf(file, length, style):
    """
    Extracts text and summarizes PDF with customization options.
    
    Args:
        file (str): Path to PDF file
        length (str): Desired summary length
        style (str): Desired output style
        
    Returns:
        str: Generated summary or error message
        
    Examples:
        >>> process_pdf("document.pdf", "detailed", "bullet points")
        '• Key point 1\n• Key point 2\n...'
    """
    if not file:
        return "⚠️ No file uploaded. Please upload a PDF."

    text = extract_text_from_pdf(file)
    if text.startswith("⚠️") or text.startswith("Error"):
        return text

    return summarize_text(text, length, style)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
        print(f"Processing PDF: {pdf_path}")
        print("\n" + "="*50)
        print("SUMMARY")
        print("="*50 + "\n")
        print(process_pdf(pdf_path, "detailed", "bullet points"))
    else:
        print("Usage: python task2.py <path_to_pdf_file>")
        print("Example: python task2.py document.pdf")