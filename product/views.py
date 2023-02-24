from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import ProductInstance


class ProductsListView(ListView):
    
    """
    View to display the product list.
    """
    
    model = ProductInstance
    template_name = 'product/store.html'
    
    def get_queryset(self):
        queryset = ProductInstance.objects.order_by('category__category').reverse()
        return queryset


class ProductView(DetailView):
    
    """
    View to display a particular product.
    """
    
    model = ProductInstance
    template_name = 'product/product.html'


class ProductsByCategory(ListView):
    
    """
    View to display the product list by categories.
    """
    
    model = ProductInstance
    template_name = 'product/category.html'
    
    def get_queryset(self):
        qs = ProductInstance.objects.filter(category__category=self.kwargs['category'])
        return qs
