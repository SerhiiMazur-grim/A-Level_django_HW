from django.shortcuts import render

# Create your views here.
def login_user(request):
    return render(request, 'user/login.html')

def register_user(request):
    return render(request, 'user/register.html')
