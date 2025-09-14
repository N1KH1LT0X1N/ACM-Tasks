import re
from datetime import datetime
from emoji import emojize

def transform_text(input_text: str) -> str:    
    number_pattern  = r"\d{5}-\d{5}"
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    input_format = "%Y-%m-%d"
    date_output_pattern = "%drd %B %Y"
    output_text = input_text
    
    list_nums = re.findall(number_pattern, input_text)    
    for num in list_nums:
        output_text = re.sub(num, "[REDACTED]", output_text)

    list_dates = re.findall(date_pattern, input_text)
    for date in list_dates:
        date_object = datetime.strptime(date, input_format)
        output_text = re.sub(date, date_object.strftime(date_output_pattern), output_text)

    list_python = re.findall(r"Python", input_text)
    for python in list_python:
        output_text = re.sub(python, emojize(":snake:"), output_text)

    return output_text

transform_text(5)

if __name__ == "__main__":
    sample_text = "Call me at 98123-45678 on 2025-08-23. I love Python more than Java."
    print(transform_text(sample_text))  