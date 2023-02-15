from django.urls import path
from .views import ProductsListView, ProductView, ProductsByCategory


urlpatterns = [
    path('product_list/', ProductsListView.as_view(), name='product_list'),
    path('product/<slug>/', ProductView.as_view(), name='product'),
    path('by_category/', ProductsByCategory.as_view(), name='by_category'),
]
