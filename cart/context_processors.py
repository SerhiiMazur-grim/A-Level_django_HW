from .models import Cart


def cart(request):
    
    """
    The function creates a basket for a logged user.
    """
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart = None
    return {'cart': cart}
