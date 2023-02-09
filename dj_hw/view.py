from django.http import  HttpRequest
from django.shortcuts import render
from blog.models import Category, Article


category = Category.objects.order_by('id')
articles = Article.objects.order_by('-id')