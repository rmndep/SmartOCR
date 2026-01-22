import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def export_txt(text, filename):
    path = f"media/{filename}.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path
def export_json(text, filename):
    path = f"media/{filename}.json"
    data = {
        "extracted_text": text
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return path
def export_pdf(text, filename):
    path = f"media/{filename}.pdf"

    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4

    x, y = 40, height - 40

    for line in text.split("\n"):
        if y < 40:
            c.showPage()
            y = height - 40

        c.drawString(x, y, line)
        y -= 14

    c.save()
    return path
