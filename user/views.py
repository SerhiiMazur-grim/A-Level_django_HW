from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserForm, UserRegistrationForm


def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Incorect username or password")
            return redirect('signin')
    else:
        form = UserForm()
        return render(request, "signin.html", {'form': form})


def signup(request):
    form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})