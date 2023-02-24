from django.urls import path

from .views import CartView, add_to_cart, OrdersList, return_order, create_order


urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('add_to_cart/<uuid:product_id>/', add_to_cart, name='add_to_cart'),
    path('orders_list/', OrdersList.as_view(), name='orders_list'),
    path('cart/create_order/', create_order, name='create_order'),
    path('order/<int:order_id>/return/', return_order, name='return_order'),
]
