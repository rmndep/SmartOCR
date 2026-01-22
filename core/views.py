from django.shortcuts import render
from core.ocr.image_ocr import extract_text_from_image
from core.ocr.text_cleaner import clean_text

def upload_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES['file']
        file_path = f"media/{uploaded_file.name}"

        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        extracted_text = ""

        if uploaded_file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            raw_text = extract_text_from_image(file_path)
            extracted_text = clean_text(raw_text)

        return render(request, 'result.html', {
            'file_name': uploaded_file.name,
            'file_path': file_path,
            'extracted_text': extracted_text
        })

    return render(request, 'upload.html')
