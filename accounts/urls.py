from django.urls import path
from .views import register_faculty

urlpatterns = [
    path('register/', register_faculty, name='register_faculty'),
]
