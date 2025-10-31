# Task 1: Text Transformer

## Overview
A Python script that applies creative transformations to text using regular expressions.

## Features
- 🕵️ **Phone Number Redaction**: Masks numbers in XXXXX-XXXXX format
- 📅 **Date Formatting**: Converts YYYY-MM-DD to readable format (e.g., 23rd August 2025)
- 🐍 **Emoji Replacement**: Converts "Python" to snake emoji

## Usage

### Basic Usage
```python
from task1 import transform_text

text = "Call me at 98123-45678 on 2025-08-23. I love Python!"
result = transform_text(text)
print(result)
# Output: Call me at [REDACTED] on 23rd August 2025. I love 🐍!
```

### Command Line
```bash
python task1.py
```

## Implementation Details

### Phone Number Pattern
- Pattern: `\d{5}-\d{5}`
- Matches: 5 digits, hyphen, 5 digits
- Example: 98123-45678 → [REDACTED]

### Date Pattern
- Pattern: `\d{4}-\d{2}-\d{2}`
- Format: YYYY-MM-DD
- Output: Ordinal format with full month name
- Examples:
  - 2025-08-23 → 23rd August 2025
  - 2025-01-01 → 1st January 2025
  - 2025-12-22 → 22nd December 2025

### Ordinal Suffix Logic
```python
if 10 <= day <= 20:
    suffix = "th"  # Special case: 11th, 12th, 13th
else:
    suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
```

## Dependencies
- `emoji>=2.0.0` - For emoji conversion

## Testing
Run the script to see example transformations:
```bash
cd task1
python task1.py
```

## Future Enhancements
- Support for international phone number formats
- Multiple date format conversions
- Configurable emoji replacements
- Email address obfuscation
- Credit card number redaction
