import re

def clean_text(text):
    """
    Cleans OCR extracted text
    """
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
