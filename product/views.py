from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import ProductInstance


class ProductsListView(ListView):
    model = ProductInstance
    template_name = 'product/store.html'
    
    def get_queryset(self):
        queryset = ProductInstance.objects.order_by('category__category').reverse()
        return queryset


class ProductView(DetailView):
    model = ProductInstance
    template_name = 'product/product.html'


class ProductsByCategory(ListView):
    model = ProductInstance
    template_name = 'product/category.html'
    
    def get_queryset(self):
        qs = ProductInstance.objects.filter(category__category=self.kwargs['category'])
        return qs
