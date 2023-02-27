from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Cart, CartItem, Order, OrderItem
from product.models import ProductInstance


class CartView(LoginRequiredMixin, View):
    
    """
    Display for the user's basket.
    """
    model = Cart
    template_name = 'cart/cart.html'

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        ctx = {
            'cart': cart
        }
        return render(request, self.template_name, ctx)


@login_required
def add_to_cart(request, product_id):
    
    """
    The feature adds to the basket a certain product is periivizing whether this 
    product is in stock and whether the user is sufficient for the user.
    """
    
    user = request.user
    cart = Cart.objects.get(user=user)
    product_instance = ProductInstance.objects.get(id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    if user.money - cart.cart_total_cost() - product_instance.price * quantity >=0:
        if product_instance.decrease_quantity(quantity):
            try:
                cart_item = cart.items.get(product_id=product_id)
                cart_item.quantity += quantity
                cart_item.save()
                messages.success(request, "Product quantity updated in cart.")
            except CartItem.DoesNotExist:
                CartItem.objects.create(cart=cart, product=product_instance, quantity=quantity)
                messages.success(request, "Product added to cart.")
            cart.cart_total_cost()
        else:
            messages.warning(request, "This product is not in stock.")

    else:
        messages.warning(request, "You don`t have enough funds.")
    return redirect(request.META.get('HTTP_REFERER'))


class OrdersList(LoginRequiredMixin, ListView):
        
    """
    Display a list of orders for the logged-in user.
    """

    model = Order
    template_name = 'cart/checkout.html'
    context_object_name = 'orders'

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset().filter(user=user).order_by('-id')
        return queryset


@login_required
def create_order(request):
    
    """
    The feature creates an order for the user according to the goods it added to the basket.
    """
    
    user = request.user
    cart = Cart.objects.get(user=user)
    if user.money - cart.cart_total_cost() >= 0:
        
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
    else:
        messages.warning(request, 'You don`t have enough funds.')
        return redirect('cart')
    
    return redirect('orders_list')


@login_required
def return_order(request, order_id):
    
    """
    The function initializes the return from the user.
    """
    
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.request_return()
        return redirect('orders_list')
    return redirect('orders_list')