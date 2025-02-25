from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage or dashboard
    path('upload/', views.upload_document, name='upload_document'),  # Upload page
    path('documents/', views.document_list, name='document_list'),  # Document listing page
    path('documents/download/<int:doc_id>/', views.download_document, name='download_document'),  # Download document
]
