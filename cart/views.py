from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Cart, CartItem, Order, OrderItem
from product.models import ProductInstance


class CartView(LoginRequiredMixin, View):
    template_name = 'cart/cart.html'

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        ctx = {
            'cart': cart
        }
        return render(request, self.template_name, ctx)

@login_required
def add_to_cart(request, product_id):
    user = request.user
    cart = Cart.objects.get(user=user)
    product_instance = ProductInstance.objects.get(id=product_id)
    if product_instance.decrease_quantity():
        try:
            cart_item = cart.items.get(product_id=product_id)
            cart_item.increment_quantity()
            messages.success(request, "Product quantity updated in cart.")
        except CartItem.DoesNotExist:
            CartItem.objects.create(cart=cart, product=product_instance)
            messages.success(request, "Product added to cart.")

        cart.cart_total_cost()

    else:
        messages.warning(request, "This product is not in stock.")
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def orders_list(request):
    user = request.user
    orders = Order.objects.filter(user=user).order_by("-id")
    return render(request, 'cart/checkout.html', {'orders': orders})

@login_required
def create_order(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    
    order = Order.objects.create(user=user, total_cost=cart.cart_total_cost())
    
    for cart_item in cart.items.all():
        OrderItem.objects.create(
            order=order, 
            product=cart_item.product, 
            quantity=cart_item.quantity, 
            item_total_cost=cart_item.get_cost())
    
    user.money -= cart.cart_total_cost()
    user.save()
    cart.items.all().delete()
    
    return redirect('orders_list')

@login_required
def return_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.request_return()
        return redirect('orders_list')
    return redirect('orders_list')