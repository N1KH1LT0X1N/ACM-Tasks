# Task 2: AI PDF Summarizer

## Overview
An AI-powered PDF summarization tool using Groq's LPU Inference Engine and Llama 3.3 70B model.

## Features
- ⚡ **Fast Processing**: Leverages Groq's LPU for near-instant summarization
- 🤖 **Powerful AI**: Uses Llama 3.3 70B for accurate summaries
- 📄 **Direct Extraction**: Processes text-based PDFs with pdfplumber
- ⚙️ **Customizable**: Adjust length and output style
- 🛡️ **Robust**: Handles errors and edge cases gracefully

## Setup

### 1. Get API Key
Get your free API key from [Groq Console](https://console.groq.com/keys)

### 2. Configure Environment
Create a `.env` file in the `task2` directory:
```env
GROQ_API_KEY=gsk_YourSecretGroqApiKeyHere
```

Or copy the example file:
```bash
cp .env.example .env
# Edit .env and add your API key
```

### 3. Install Dependencies
```bash
pip install -r ../requirements.txt
```

## Usage

### Command Line
```bash
python task2.py path/to/document.pdf
```

### In Python Code
```python
from task2 import process_pdf

# Basic usage
summary = process_pdf("document.pdf", "detailed", "bullet points")
print(summary)

# Custom options
summary = process_pdf(
    "research_paper.pdf",
    length="brief",
    style="paragraph"
)
```

## Customization Options

### Length Options
- `"brief"` - Short, concise summary
- `"detailed"` - Comprehensive summary
- Custom: Any descriptive length (e.g., "medium", "extensive")

### Style Options
- `"bullet points"` - Structured list format
- `"paragraph"` - Flowing narrative
- `"numbered list"` - Numbered points
- Custom: Any format description

## How It Works

1. **Text Extraction**: Uses `pdfplumber` to extract text from PDF
2. **Prompt Construction**: Builds structured prompt for AI model
3. **AI Processing**: Groq API processes with Llama 3.3 70B
4. **Result Formatting**: Returns clean, structured summary

## Limitations

- Only works with text-based PDFs (not scanned/image PDFs)
- Input limited to 10,000 characters for efficiency
- Requires active internet connection for API calls
- API rate limits apply (check Groq documentation)

## Error Handling

The tool handles various edge cases:
- **Missing API Key**: Clear error message with setup instructions
- **Invalid PDF**: Catches and reports extraction errors
- **Scanned PDFs**: Warns when no readable text found
- **Network Issues**: Reports connection problems

## Examples

### Example 1: Research Paper
```bash
python task2.py research_paper.pdf
```
Output: Detailed bullet-point summary of key findings

### Example 2: Report Document
```python
from task2 import process_pdf
summary = process_pdf("annual_report.pdf", "brief", "paragraph")
```

## Troubleshooting

### "GROQ_API_KEY is not set"
- Ensure `.env` file exists in `task2` directory
- Check API key is properly formatted
- Verify no extra spaces or quotes

### "No readable text found"
- PDF might be scanned/image-based
- Try converting to text-based PDF first
- Use OCR tools if needed

### Import Errors
```bash
pip install --upgrade -r requirements.txt
```

## Future Enhancements
- OCR support for scanned PDFs
- Multiple PDF batch processing
- Summary quality scoring
- Export to various formats (MD, TXT, JSON)
- Caching for repeated summarizations
- Support for other LLM providers
