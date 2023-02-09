from django.http import  HttpRequest, Http404
from django.shortcuts import render


def signin(request: HttpRequest):
    return  render(request, 'signin.html')

def signup(request: HttpRequest):
    return  render(request, 'signup.html')
