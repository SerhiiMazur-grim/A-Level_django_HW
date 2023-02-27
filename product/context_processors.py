from .models import Category


def categories(request):
    
    """
    The function transmits queriset categories for their reflection in the navigation panel.
    """
    
    return {'categories': Category.objects.order_by('id')}
