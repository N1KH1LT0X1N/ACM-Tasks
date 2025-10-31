"""
Text Transformer Module

This module provides functionality to transform text by:
- Redacting phone numbers in format XXXXX-XXXXX
- Formatting dates from YYYY-MM-DD to readable format (e.g., 23rd August 2025)
- Replacing "Python" with snake emoji 🐍

Author: Nikhil Toxin
Created for: DJSCE ACM Research Club Technical Interview 2025
"""

import re
from datetime import datetime
from emoji import emojize

def transform_text(input_text: str) -> str:
    """
    Apply multiple transformations to input text.
    
    Args:
        input_text (str): The text to transform
        
    Returns:
        str: The transformed text with all modifications applied
        
    Examples:
        >>> transform_text("Call me at 98123-45678 on 2025-08-23. I love Python!")
        'Call me at [REDACTED] on 23rd August 2025. I love 🐍!'
        
    Transformations applied:
        1. Redacts phone numbers matching pattern XXXXX-XXXXX
        2. Converts dates from YYYY-MM-DD to ordinal format
        3. Replaces "Python" with snake emoji
    """    
    number_pattern  = r"\d{5}-\d{5}"
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    input_format = "%Y-%m-%d"
    output_text = input_text
    
    # Redact phone numbers
    list_nums = re.findall(number_pattern, input_text)    
    for num in list_nums:
        output_text = re.sub(num, "[REDACTED]", output_text)

    # Format dates with proper ordinal suffixes
    list_dates = re.findall(date_pattern, input_text)
    for date in list_dates:
        date_object = datetime.strptime(date, input_format)
        day = date_object.day
        
        # Determine ordinal suffix
        if 10 <= day <= 20:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
        
        formatted_date = date_object.strftime(f"%d{suffix} %B %Y")
        output_text = re.sub(date, formatted_date, output_text)

    # Replace Python with snake emoji
    list_python = re.findall(r"Python", input_text)
    for python in list_python:
        output_text = re.sub(python, emojize(":snake:"), output_text)

    return output_text

if __name__ == "__main__":
    # Example usage
    sample_text = "Call me at 98123-45678 on 2025-08-23. I love Python more than Java."
    print("Original Text:")
    print(sample_text)
    print("\nTransformed Text:")
    print(transform_text(sample_text))  