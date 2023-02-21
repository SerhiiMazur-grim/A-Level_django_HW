from django import forms

from product.models import ProductInstance


class CreateProduct(forms.ModelForm):
    class Meta:
        model = ProductInstance
        fields = ('title', 'category', 'description', 'price', 'quantity')
