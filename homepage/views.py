from django.shortcuts import render
from product.models import Category


def home(request):
    """render home page"""
    ctx = {
        'categories': Category.objects.order_by('id'),
    }
    return render(request, 'homepage/homepage.html', ctx)
