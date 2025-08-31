Of course\! Here is a comprehensive GitHub README file for your AI-powered PDF summarizer script.

-----

# 📄 AI PDF Summarizer

A powerful Python script to quickly summarize your PDF documents using the blazingly fast **Groq API** and the **Llama 3.3 70B model** via LangChain.

This tool extracts text directly from PDF files and generates a concise, well-structured summary, saving you valuable time and effort.

-----

## ✨ Features

  * **Fast Summarization**: Leverages the Groq LPU™ Inference Engine for near-instant summary generation.
  * **High-Quality Model**: Utilizes the powerful `llama-3.3-70b-versatile` model for accurate and coherent summaries.
  * **Direct PDF Processing**: Extracts text directly from text-based PDF files using `pdfplumber`.
  * **Customizable Output**: Easily adjust the desired **length** (e.g., "brief", "detailed") and **style** (e.g., "paragraph", "bullet points") of the summary.
  * **Robust Error Handling**: Gracefully handles non-existent files and PDFs without readable text (e.g., scanned documents).
  * **Easy to Use**: Can be run directly from the command line with a simple argument.

-----

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1\. Prerequisites

  * Python 3.8+
  * Git

### 2\. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 3\. Install Dependencies

It's recommended to use a virtual environment.

```bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate
# Activate it (macOS/Linux)
source venv/bin/activate
```

Install the required Python packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, create one with the following content:

```txt
python-dotenv
pdfplumber
langchain-groq
langchain
```

### 4\. Set Up API Key

This project requires an API key from Groq.

1.  Get your free API key at [Groq Console](https://console.groq.com/keys).

2.  Create a file named `.env` in the root directory of the project.

3.  Add your API key to the `.env` file like this:

    ```env
    GROQ_API_KEY="gsk_YourSecretGroqApiKeyHere"
    ```

-----

## 🛠️ Usage

You can use the script directly from the command line or integrate its functions into your own applications.

### As a Command-Line Tool

To summarize a PDF, run the script and pass the path to your PDF file as an argument.

```bash
python your_script_name.py "/path/to/your/document.pdf"
```

The script will print the summary directly to the console. The default summary is "detailed" and formatted in "bullet points".

### As a Module

You can import the `process_pdf` function to use the summarizer within your own Python code. This allows for more control over the output style and length.

```python
from your_script_name import process_pdf

# Define the path to your PDF and desired summary options
pdf_path = "reports/annual_report_2024.pdf"
summary_length = "brief" # Options: "brief", "detailed", etc.
summary_style = "paragraph" # Options: "paragraph", "bullet points", etc.

# Get the summary
summary = process_pdf(pdf_path, summary_length, summary_style)

# Print the result
print("--- Summary ---")
print(summary)
```

-----

## 🧠 How It Works

The script follows a simple three-step process:

1.  **Extract Text**: The `extract_text_from_pdf` function uses `pdfplumber` to open the PDF and extract all text content. It handles multi-page documents and returns a clean string.
2.  **Construct Prompt**: The `summarize_text` function takes the extracted text and builds a carefully structured prompt. This prompt instructs the Llama 3.3 model on how to reason and what format to use for the output.
3.  **Generate Summary**: The prompt is sent to the Groq API via the `ChatGroq` client. The powerful and efficient LPU Inference Engine processes the request and returns the final summary.