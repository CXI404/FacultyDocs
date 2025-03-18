from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FacultyUser
# Register your models here.


class FacultyAdmin(UserAdmin):
    list_display = ('username','email','faculty_id','is_approved')
    list_filter = ('is_approved',)
    actions = ['approve_users']



    def approve_users(self,request,queryset):
        queryset.update(is_approved=True)


admin.site.register(FacultyUser,FacultyAdmin)
