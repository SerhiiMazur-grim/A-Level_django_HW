from django.urls import path

from .views import ProdListAdmin, CreateProdAdmin, UpdateProdAdmin, OrderListAdmin, return_money, decline_return

urlpatterns = [
    path('product_list_admin/', ProdListAdmin.as_view(), name='product_list_admin'),
    path('order_list_admin/', OrderListAdmin.as_view(), name='order_list_admin'),
    path('create_product_admin/', CreateProdAdmin.as_view(), name='create_product_admin'),
    path('<pk>/update/', UpdateProdAdmin.as_view(), name='update_product_admin'),
    path('return_money/<int:order_id>', return_money, name='return_money'),
    path('decline_return/<int:order_id>', decline_return, name='decline_return'),
]