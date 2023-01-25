from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render

def log_in(request: HttpRequest):
    return render(request, 'login.html')


def reg_user(request: HttpRequest):
    return render(request, 'registration.html')
