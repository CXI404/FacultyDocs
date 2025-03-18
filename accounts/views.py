from django.shortcuts import render,redirect
from .forms import FacultyRegistrationForm
from django.contrib.auth import login



def register_faculty(request):
    if request.method=="POST":
        form=FacultyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save immediately
            user.is_active = False  # Disable login until approved
            user.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = FacultyRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

def login_faculty(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_approved:
            login(request, user)
            return redirect('faculty_dashboard')
        else:
            messages.error(request, "Invalid credentials or account not approved")
    return render(request, 'accounts/login.html')

def logout_faculty(request):
    logout(request)
    return redirect('login')




from django.contrib.auth.decorators import login_required

@login_required
def faculty_dashboard(request):
    return render(request, 'accounts/dashboard.html')