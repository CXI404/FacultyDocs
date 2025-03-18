from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class FacultyUser(AbstractUser):
    is_approved=models.BooleanField(default=False)#Admin must approve faculty
    faculty_id=models.CharField(max_length=20,unique=True)#Unique faculty id

    def __str__(self):
        return self.username