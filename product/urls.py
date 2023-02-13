from django.urls import path
from .views import prod_list, product


urlpatterns = [
    path('product_list/', prod_list, name='product_list'),
    path('product/', product, name='product'),
]
