from django.http import  HttpRequest, Http404
from django.shortcuts import render

from blog.models import Article, Category


def home_page(request: HttpRequest):
    ctx = {
        'categorys_list': Category.objects.order_by('id'), 
        'article_list': Article.objects.order_by('-id'),
    }
    return  render(request, 'homepage.html', ctx)


def article_page(request: HttpRequest, id):
        try:
            article = Article.objects.get(id=id)
            ctx = {
                'categorys_list': Category.objects.order_by('id'), 
                'article': article,
            }
            return render(request, 'blogpost.html', ctx)
        except:
            raise Http404('Can`t find this object!')


def article_by_category(request: HttpRequest, select_category):
    try:
        articles = Article.objects.filter(category=Category.objects.get(category=select_category))
        ctx = {
            'select_category': select_category,
            'categorys_list': Category.objects.order_by('id'),
            'article_list': articles
        }
        return  render(request, 'article_by_category.html', ctx)
    except:
        raise Http404('Can`t find this category!')
