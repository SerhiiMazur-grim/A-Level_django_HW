from django.db import models
from django.shortcuts import redirect

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
    
    def get_items_ids(self):
        qs = [i.product.id for i in self.get_items()]
        return qs

    def get_total_cart(self):
        total = sum([item.get_total() for item in self.get_items()])
        return total
    
    def clear_cart(self):
        for item in self.get_items():
            item.delete()
        self.save()
        
    


class CartItem(models.Model):
    product = models.ForeignKey(ProductInstance, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return  self.product.title

    def get_total(self):
        total = self.product.price * self.quantity
        return total


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user) + ' - ' + str(self.id)
    
    def save_cart_items(self):
        cart = Cart.objects.get(user=self.user)
        for item in cart.get_items():
            obj = OrderItems(
                product = item.product,
                order = self,
                quantity = item.quantity
                )
            obj.save()
        cart.clear_cart()

    def get_items(self):
        qs = OrderItems.objects.filter(order=self.id)
        return qs

    def get_total_order(self):
        total = sum([item.get_total() for item in self.get_items()])
        return total



class OrderItems(models.Model):
    product = models.ForeignKey(ProductInstance, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return  self.product.title
    
    def get_total(self):
        total = self.product.price * self.quantity
        return total



