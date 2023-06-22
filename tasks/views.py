from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def hello_world(request):
  return render(request, 'signup.html', {
    'user_form': UserCreationForm()
  })
