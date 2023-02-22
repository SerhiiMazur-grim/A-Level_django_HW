from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin


from product.models import ProductInstance
from cart.models import Order
from .forms import CreateProduct


class ProdListAdmin(UserPassesTestMixin, ListView):
    template_name = 'admin_view/prod_list.html'
    model = ProductInstance
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def get_queryset(self):
        return self.model.objects.order_by('-pk')


class CreateProdAdmin(UserPassesTestMixin, CreateView):
    template_name = 'admin_view/add_prod.html'
    success_url = reverse_lazy('product_list_admin')
    form_class = CreateProduct
    
    def test_func(self):
        return self.request.user.is_superuser
    
    
class UpdateProdAdmin(UserPassesTestMixin, UpdateView):
    template_name = 'admin_view/update_prod.html'
    success_url = reverse_lazy('product_list_admin')
    form_class = CreateProduct
    model = ProductInstance
    
    def test_func(self):
        return self.request.user.is_superuser


class OrderListAdmin(UserPassesTestMixin, ListView):
    template_name = 'admin_view/orders_list.html'
    model = Order
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def get_queryset(self):
        return self.model.objects.order_by('-pk')


@user_passes_test(lambda u: u.is_staff)
def return_money(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST' and order.is_returned == None:
        order.return_order()
        return redirect('order_list_admin')
    return redirect('order_list_admin')


@user_passes_test(lambda u: u.is_staff)
def decline_return(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST' and order.is_returned == None:
        order.is_returned = False
        order.save()
        return redirect('order_list_admin')
    return redirect('order_list_admin')
