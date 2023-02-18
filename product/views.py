from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import ProductInstance
from cart.models import CartItem, Cart
from django.shortcuts import render, redirect


class ProductsListView(ListView):
    model = ProductInstance
    template_name = 'product/store.html'


class ProductView(DetailView):
    model = ProductInstance
    template_name = 'product/product.html'


class ProductsByCategory(ListView):
    model = ProductInstance
    template_name = 'product/category.html'
    
    def get_queryset(self):
        qs = ProductInstance.objects.filter(category__category=self.kwargs['category'])
        return qs
