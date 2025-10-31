# ACM Research Interview Tasks

This repository contains my solutions for the **DJSCE ACM Research Club – Technical Interview 2025** tasks.  
The tasks cover Python programming, text processing, and reflective writing. The goal of this repository is to showcase problem-solving, creativity, and structured documentation.

## 📋 Progress Overview

- **Total Tasks:** 4  
- **Completed:** 4 ✅
- **Remaining:** 0

| Task Number | Status     | Description |
|-------------|------------|-------------|
| Task 1 (Python) | ✅ Complete  | Mischievous Text Transformer |
| Task 2 (Python) | ✅ Complete  | Extract Structure from Unstructured Text |
| Task 3 (Writing) | ✅ Complete  | Blog Review – Assigned Reading |
| Task 4 (Writing) | ✅ Complete  | Blog Review – Open Ended |

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

**📖 Need detailed installation help? See [INSTALLATION.md](INSTALLATION.md)**

### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/N1KH1LT0X1N/ACM-Tasks.git
   cd ACM-Tasks
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **For Task 2 (PDF Summarizer), set up your Groq API key:**
   - Get your free API key from [Groq Console](https://console.groq.com/keys)
   - Create a `.env` file in the `task2` directory:
     ```env
     GROQ_API_KEY=your_api_key_here
     ```
   - **⚠️ SECURITY:** Never commit your `.env` file! It's already in `.gitignore`
   - See [SECURITY_CHECKLIST.md](SECURITY_CHECKLIST.md) for security best practices

## 🔒 Security

```
ACM-Tasks/
├── task1/                    # Text Transformer
│   ├── task1.py             # Main Python script
│   ├── task_readme.md       # Task description
│   └── solution.md          # Documentation
├── task2/                    # PDF Summarizer
│   ├── task2.py             # Main Python script
│   ├── task_readme.md       # Task description
│   ├── solution.md          # Documentation
│   └── .gitignore           # Ignore PDFs and .env
├── task3/                    # Blog Review (Assigned)
│   ├── task_readme.md       # Task description
│   └── solution.md          # My review
├── task4/                    # Blog Review (Open-ended)
│   ├── task_readme.md       # Task description
│   └── solution.md          # My review
├── .gitignore               # Global ignore file
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## 🛠️ Usage

### Task 1: Text Transformer
Transform text with redactions, date formatting, and emoji replacements:

```bash
cd task1
python task1.py
```

**Example:**
```python
from task1 import transform_text

text = "Call me at 98123-45678 on 2025-08-23. I love Python more than Java."
result = transform_text(text)
print(result)
# Output: Call me at [REDACTED] on 23rd August 2025. I love 🐍 more than Java.
```

### Task 2: AI PDF Summarizer
Summarize PDF documents using AI:

```bash
cd task2
python task2.py path/to/your/document.pdf
```

**Features:**
- Extracts text from text-based PDFs
- Generates structured summaries using Llama 3.3 70B model
- Customizable output length and style

## 🎯 Key Features

### Task 1: Text Transformer
- 🕵️ **Redacts sensitive information** (phone numbers)
- 📅 **Reformats dates** to readable format
- 🐍 **Emojifies keywords** (Python → 🐍)
- Uses regex patterns for flexible text processing

### Task 2: PDF Summarizer
- ⚡ **Fast processing** with Groq LPU Inference Engine
- 🤖 **AI-powered** using Llama 3.3 70B model
- 📄 **Direct PDF extraction** with pdfplumber
- ⚙️ **Customizable output** formats
- 🛡️ **Robust error handling**

### Task 3 & 4: Blog Reviews
- 📚 Critical analysis of technical blogs
- 💡 Reflective learning documentation
- 🔗 Connection to research interests

## 🤝 Contributing

While this is a personal interview submission, suggestions and feedback are welcome! Feel free to open an issue or reach out.

## 📝 License

This project is created for educational purposes as part of the DJSCE ACM Research Club interview process.

## 👤 Author

**Nikhil Toxin**
- GitHub: [@N1KH1LT0X1N](https://github.com/N1KH1LT0X1N)
- Repository: [ACM-Tasks](https://github.com/N1KH1LT0X1N/ACM-Tasks)

## 📚 Additional Resources

- [📖 Installation Guide](INSTALLATION.md) - Detailed setup instructions
- [� Security Checklist](SECURITY_CHECKLIST.md) - Pre-commit security verification
- [🔒 Security Audit Report](SECURITY_AUDIT_REPORT.md) - Complete security audit
- [�📊 Project Stats](STATS.md) - Repository statistics and metrics
- [📝 Changelog](CHANGELOG.md) - Version history and updates
- [🔒 Security Policy](SECURITY.md) - Security practices and reporting
- [🤝 Contributing](CONTRIBUTING.md) - How to contribute
- [⚖️ License](LICENSE) - MIT License details

## 🙏 Acknowledgments

- DJSCE ACM Research Club for providing these interesting challenges
- Groq for their amazing LPU Inference Engine
- The open-source community for the excellent libraries used in this project

---

⭐ If you find this repository helpful, please consider giving it a star!
