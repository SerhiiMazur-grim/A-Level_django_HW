from django import forms

from product.models import ProductInstance


class CreateProduct(forms.ModelForm):
    
    """
    A form to create a product.
    """
    
    class Meta:
        model = ProductInstance
        fields = ('title', 'category', 'description', 'price', 'quantity')
