from django.db import models

class Document(models.Model):
    CATEGORY_CHOICES = [
        ('research_paper', 'Research Paper'),
        ('thesis', 'Thesis'),
        ('certificate', 'Certificate'),
        ('other', 'Other'),
    ]

    faculty_name = models.CharField(max_length=100)  # Faculty name
    title = models.CharField(max_length=255)  # Document title
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')  # Category
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    file = models.FileField(upload_to='uploads/')  # File storage

    def __str__(self):
        return f"{self.faculty_name} - {self.title} ({self.category})"
