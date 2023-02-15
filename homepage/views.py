from django.shortcuts import render
from product.models import Category
from django.views.generic import ListView
from product.models import Category, ProductInstance


class HomeView(ListView):
    model = ProductInstance
    extra_context = {'categories': Category.objects.order_by('id'),}
    template_name = 'homepage/homepage.html'



# def home(request):
#     """render home page"""
#     ctx = {
#         'categories': Category.objects.order_by('id'),
#     }
#     return render(request, 'homepage/homepage.html', ctx)
