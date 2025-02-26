from django.shortcuts import render, redirect
from .forms import DocumentForm





def upload_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)  # Uses ModelForm
        if form.is_valid():
            form.save()  # Saves faculty name, title, file, and category
            return redirect('upload_success')
    else:
        form = DocumentForm()

    return render(request, 'uploads/upload.html', {'form': form})


def upload_success(request):
    return render(request, 'uploads/success.html')  # Corrected template path


from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, this is the uploads home page!")


from django.shortcuts import render
from .models import Document

from django.shortcuts import render
from .models import Document


def document_list(request):
    category = request.GET.get('category', '')  # Get category filter from URL
    if category:
        documents = Document.objects.filter(category=category).order_by('-uploaded_at')  # Filter and order
    else:
        documents = Document.objects.all().order_by('-uploaded_at')  # Fetch all and order by latest

    categories = Document.objects.values_list('category', flat=True).distinct()  # Get unique categories
    return render(request, 'uploads/document_list.html', {'documents': documents, 'categories': categories})


from django.shortcuts import get_object_or_404
from django.http import FileResponse
from .models import Document  # Import your model

def download_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    return FileResponse(document.file.open(), as_attachment=True)
