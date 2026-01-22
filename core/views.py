from django.shortcuts import render

def upload_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES['file']

        file_path = f"media/{uploaded_file.name}"

        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        return render(request, 'result.html', {
            'file_name': uploaded_file.name,
            'file_path': file_path
        })

    return render(request, 'upload.html')
