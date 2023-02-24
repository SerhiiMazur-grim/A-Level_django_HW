from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from .forms import SignInForm, SignUpForm


def signin(request):
    """
    Sign in function
    """
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    form = SignInForm()
    return render(request, "signin.html", {'form': form})


def signup(request):
    """
    Sign up function
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_logout(request):
    """
    Logout user
    """
    logout(request)
    return redirect('signin')
