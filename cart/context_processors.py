from .models import Cart


def cart(request):
    try:
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user, complete=False)
        return {'cart': cart}
    except:
        return {'cart': None}
