from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Category, ProductInstance


class ProductsListView(ListView):
    model = ProductInstance
    extra_context = {'categories': Category.objects.order_by('id'),}
    template_name = 'product/store.html'


class ProductView(DetailView):
    model = ProductInstance
    extra_context = {'categories': Category.objects.order_by('id'),}
    template_name = 'product/product.html'


class ProductsByCategory(ListView):
    model = ProductInstance
    extra_context = {'categories': Category.objects.order_by('id'),}
    template_name = 'product/category.html'
    
    def get_queryset(self):
        qs = ProductInstance.objects.filter(category__category=self.kwargs['category'])
        return qs