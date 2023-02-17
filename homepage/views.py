from django.views.generic import ListView

from product.models import ProductInstance


class HomeView(ListView):
    model = ProductInstance
    template_name = 'homepage/homepage.html'
