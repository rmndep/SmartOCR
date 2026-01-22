from django.shortcuts import render
from core.ocr.image_ocr import extract_text_from_image
from core.ocr.text_cleaner import clean_text
from core.ocr.pdf_ocr import extract_text_from_pdf
from core.ai.summarizer import summarize_text
from core.export.exporter import export_txt, export_json, export_pdf
from django.http import FileResponse


def upload_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES['file']
        file_path = f"media/{uploaded_file.name}"

        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        extracted_text = ""

        # 🔹 STEP 1: OCR
        if uploaded_file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            raw_text = extract_text_from_image(file_path)
            extracted_text = clean_text(raw_text)

        elif uploaded_file.name.lower().endswith('.pdf'):
            extracted_text = extract_text_from_pdf(file_path)

        print("OCR TEXT:", repr(extracted_text))

        # 🔹 STEP 2: AI SUMMARY
        summarize = request.POST.get("summarize")
        summary = None

        if summarize and extracted_text.strip():
            summary = summarize_text(extracted_text)

        # 🔹 STEP 3: EXPORT
        export_type = request.POST.get("export")
        export_file = None

        if export_type == "txt":
            export_file = export_txt(extracted_text, uploaded_file.name)

        elif export_type == "json":
            export_file = export_json(extracted_text, uploaded_file.name)

        elif export_type == "pdf":
            export_file = export_pdf(extracted_text, uploaded_file.name)

        # ✅ THIS WAS MISSING
        if export_file:
            return FileResponse(
                open(export_file, "rb"),
                as_attachment=True
            )

        # 🔹 STEP 4: NORMAL PAGE RENDER
        return render(request, 'result.html', {
            'file_name': uploaded_file.name,
            'file_path': file_path,
            'extracted_text': extracted_text,
            'summary': summary
        })

    return render(request, 'upload.html')
