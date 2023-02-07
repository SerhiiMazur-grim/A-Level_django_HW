from django.http import  HttpRequest, Http404
from django.shortcuts import render
from blog.models import Category, Article


category = Category.objects.order_by('id')
articles = Article.objects.order_by('-id')


def home_page(request: HttpRequest):
    ctx = {
        'categorys_list': category, 
        'article_list': articles,
    }
    return  render(request, 'homepage.html', ctx)


def article_page(request: HttpRequest, id):
        for article in articles:
            if article.id == id:
                ctx = {
                    'categorys_list': category, 
                    'article': article,
                }
                return render(request, 'blogpost.html', ctx)
        raise Http404('Can`t find this object!')


def article_by_category(request: HttpRequest, select_category):
    articles = [i for i in Article.objects.all() if str(i.category) == select_category]
    ctx = {
        'select_category': select_category,
        'categorys_list': category,
        'article_list': articles
    }
    return  render(request, 'article_by_category.html', ctx)