from django.db import models

from user.models import CustomUser
from product.models import ProductInstance


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    added_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user)

    def __len__(self):
        len = self.get_items().count()
        return len

    def get_items(self):
        qs = CartItem.objects.filter(cart=self.id)
        return qs

    def get_total_cart(self):
        total = sum([item.get_total() for item in self.get_items()])
        return total


class CartItem(models.Model):
    product = models.ForeignKey(ProductInstance, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return  self.product.title

    def get_total(self):
        total = self.product.price * self.quantity
        return total


