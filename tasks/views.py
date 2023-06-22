from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError

# Create your views here.

def home(request):
  return render(request, 'home.html')


def signup(request):
  if request.method == 'GET':
    return render(request, 'signup.html', {
      'user_form': UserCreationForm()
    })
  else:
    if request.POST['password1'] == request.POST['password2']:
      try:
        user = User.objects.create_user(
          username=request.POST['username'],
          password=request.POST['password1']
        )
        user.save()
        login(request, user)
        return redirect('tasks')
      except IntegrityError:
        return render(request, 'signup.html', {
          'user_form': UserCreationForm(),
          'error': 'Username already exists'
        })
    return render(request, 'signup.html', {
      'user_form': UserCreationForm(),
      'error': 'Passwords do not match'
    })


def tasks(request):
  return render(request, 'tasks.html')


def signout(request):
  logout(request)
  return redirect('home')
