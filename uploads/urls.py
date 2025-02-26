from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='uploads_home'),  # Home page for /uploads/
    path('upload/', views.upload_document, name='upload_document'),  # Upload page
    path('documents/', views.document_list, name='document_list'),  # Document listing page
    path('documents/download/<int:doc_id>/', views.download_document, name='download_document'),
    path('success/', views.upload_success, name='success'), # Download document
]
