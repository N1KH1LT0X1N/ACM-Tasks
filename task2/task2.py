import os
import sys
from dotenv import load_dotenv
import pdfplumber
from langchain_groq.chat_models import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set. Add it in Hugging Face Secrets.")

llm = ChatGroq(model_name="llama-3.3-70b-versatile")

def extract_text_from_pdf(pdf_file):
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
    """Summarizes extracted text with structured formatting."""
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
    """Extracts text and summarizes PDF with customization options."""
    if not file:
        return "⚠️ No file uploaded. Please upload a PDF."

    text = extract_text_from_pdf(file)
    if text.startswith("⚠️") or text.startswith("Error"):
        return text

    return summarize_text(text, length, style)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(f"PDF Captured : \nSummary : \n\n {process_pdf(sys.argv[1], "detailed", "bullet points")}")
    else:
        print("No arguments provided for pdf file.")