from django.views.generic import ListView

from product.models import ProductInstance


class HomeView(ListView):
    model = ProductInstance
    template_name = 'homepage/homepage.html'
    
    def get_queryset(self):
        queryset = ProductInstance.objects.order_by('category__category').reverse()
        return queryset
