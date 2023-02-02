from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')



def main_registration(request):
    return render(request, 'registration/main_registration.html')