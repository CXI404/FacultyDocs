from django import forms
from .models import Document  # Import the Document model

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'category','file','faculty_name']
