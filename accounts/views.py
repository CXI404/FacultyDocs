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
