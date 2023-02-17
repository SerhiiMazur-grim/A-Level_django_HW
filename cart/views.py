from django.shortcuts import render
from django.views.generic import ListView

from .models import Cart, CartItem

def checkout(request):
    # user = request.user
    # cart, created = Cart.objects.get_or_create(user=user, complete=False)
    # ctx = {
    #     'cart': cart,
    # }
    return render(request, 'cart/checkout.html')

# class CartListView(ListView):
#     model = Cart
#     extra_context = {'categories': Category.objects.order_by('id'),}
#     template_name = 'cart/checkout.html'