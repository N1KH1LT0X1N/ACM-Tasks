# Installation Guide

## Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package installer (comes with Python)
- **Git** - [Download Git](https://git-scm.com/downloads)

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/N1KH1LT0X1N/ACM-Tasks.git
cd ACM-Tasks
```

### 2. Create Virtual Environment (Recommended)

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `emoji>=2.0.0` - For Task 1
- `python-dotenv>=1.0.0` - For Task 2
- `pdfplumber>=0.10.0` - For Task 2
- `langchain-groq>=0.1.0` - For Task 2
- `langchain>=0.1.0` - For Task 2

### 4. Verify Installation

Test Task 1:
```bash
cd task1
python task1.py
```

You should see example output showing text transformations.

### 5. Configure Task 2 (PDF Summarizer)

#### Get API Key
1. Visit [Groq Console](https://console.groq.com/keys)
2. Sign up for a free account
3. Generate a new API key

#### Set Up Environment
```bash
cd task2
```

**Option A: Copy example file**
```bash
# Windows PowerShell
Copy-Item .env.example .env

# macOS/Linux
cp .env.example .env
```

**Option B: Create manually**
Create a file named `.env` in the `task2` directory:
```env
GROQ_API_KEY=gsk_YourActualApiKeyHere
```

**Important**: Replace `gsk_YourActualApiKeyHere` with your actual API key!

### 6. Test Task 2

```bash
# From task2 directory
python task2.py
```

You should see usage instructions.

## Troubleshooting

### Python Not Found
**Error**: `'python' is not recognized as an internal or external command`

**Solution**: 
- Ensure Python is installed and added to PATH
- Try `python3` instead of `python`
- Restart terminal after installation

### Permission Errors (Windows)
**Error**: `cannot be loaded because running scripts is disabled`

**Solution**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Module Not Found
**Error**: `ModuleNotFoundError: No module named 'emoji'`

**Solution**:
```bash
pip install -r requirements.txt
```

### API Key Not Working
**Error**: `GROQ_API_KEY is not set`

**Checklist**:
- [ ] `.env` file exists in `task2` directory (not project root)
- [ ] API key is on the line: `GROQ_API_KEY=your_key`
- [ ] No spaces around the `=` sign
- [ ] No quotes around the key value
- [ ] File is named `.env` not `env.txt` or `.env.txt`

### Virtual Environment Issues
**Can't activate venv**

**Windows PowerShell**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

**If still not working**, install packages globally (not recommended for production):
```bash
pip install -r requirements.txt
```

## Platform-Specific Notes

### Windows
- Use PowerShell (recommended) or Command Prompt
- Some antivirus software may flag Python scripts - add exception if needed

### macOS
- May need to use `python3` and `pip3` instead of `python` and `pip`
- If permission denied: `chmod +x task1/task1.py task2/task2.py`

### Linux
- Usually comes with Python pre-installed
- May need to install pip separately: `sudo apt install python3-pip`
- Use `python3` and `pip3` commands

## Verifying Installation

Run this command to check all dependencies:
```bash
pip list
```

You should see:
- emoji
- python-dotenv
- pdfplumber
- langchain-groq
- langchain

## Uninstallation

To remove the virtual environment and clean up:

```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment folder
# Windows
Remove-Item -Recurse -Force venv

# macOS/Linux
rm -rf venv
```

## Need Help?

- Check [README.md](README.md) for usage instructions
- See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines
- Open an issue on GitHub if problems persist

---

**Installation successful? You're ready to explore the tasks!** 🎉
