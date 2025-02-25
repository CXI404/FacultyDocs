from django import forms
from .models import Document  # Import the Document model

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['faculty_name', 'title', 'document_type', 'file']
