from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import FacultyUser

class FacultyRegistrationForm(UserCreationForm)
    faculty_id=forms.CharField(max_length=20)


    class Meta:
        model=FacultyUser
        fields=['username','email','faculty_id','password1','password2']