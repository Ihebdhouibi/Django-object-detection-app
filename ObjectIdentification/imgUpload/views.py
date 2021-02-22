from django.shortcuts import render

from .form import ImageUploadForm


def handle_uploaded_files(f):
    with open('img.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# Create your views here.
def home(request):
    return render(request, 'home.html')


def imageprocess(request):
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
        handle_uploaded_files(request.FILES['image'])
    return render(request, 'result.html')
