from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from product.models import ProductInstance
from .models import Cart, CartItem, Order, OrderItems


@login_required
def cart(request):
    return render(request, 'cart/cart.html')

@login_required
def checkout(request):
    user = request.user
    order = Order.objects.filter(user=user)
    return render(request, 'cart/checkout.html', {'order': order})



@login_required
def add(request, cart_id, prod_id):
    product = ProductInstance.objects.get(id=prod_id)
    cart = Cart.objects.get(id=cart_id)
    if product.count > 0:
        if product.id in cart.get_items_ids():
            obj = CartItem.objects.get(product = product.id)
            obj.quantity += 1
            obj.save()
        else:
            obj = CartItem(
                product = product,
                cart = cart,
                quantity = 1
            )
            obj.save()
    else:
        pass
    return redirect(request.META['HTTP_REFERER'])

@login_required
def order(request):
        user = request.user
        order= Order.objects.create(user=user)
        order.save_cart_items()
        return redirect('checkout')

@login_required
def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect(request.META['HTTP_REFERER'])
