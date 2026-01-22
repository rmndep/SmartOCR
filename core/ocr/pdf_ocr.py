import fitz  # PyMuPDF
from pdf2image import convert_from_path
from core.ocr.image_ocr import extract_text_from_image
from core.ocr.text_cleaner import clean_text
import os
import uuid
def is_text_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    for page in doc:
        if page.get_text().strip():
            return True
    return False
def extract_text_from_text_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return clean_text(text)
def extract_text_from_scanned_pdf(pdf_path):
    pages = convert_from_path(pdf_path, dpi=300)

    full_text = ""

    for page in pages:
        temp_image = f"media/temp_{uuid.uuid4()}.png"
        page.save(temp_image, "PNG")

        text = extract_text_from_image(temp_image)
        full_text += text + "\n"

        os.remove(temp_image)

    return clean_text(full_text)
def extract_text_from_pdf(pdf_path):
    if is_text_pdf(pdf_path):
        return extract_text_from_text_pdf(pdf_path)
    else:
        return extract_text_from_scanned_pdf(pdf_path)
