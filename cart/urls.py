from django.urls import path

from .views import cart, add, checkout, delete_order, order


urlpatterns = [
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('cart/add/<int:cart_id>/<uuid:prod_id>', add, name='add'),
    path('order/delete/<int:order_id>/', delete_order, name='delete_order'),
    path('order/create/', order, name='order'),
]
