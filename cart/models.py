from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

from user.models import CustomUser
from product.models import ProductInstance


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.user} - {self.id}'
    
    def __len__(self):
        return self.items.count()

    def get_absolute_url(self):
        return reverse('cart_detail', args=[self.id])

    def cart_total_cost(self):
        self.total = sum(item.get_cost() for item in self.items.all())
        self.save()
        return self.total



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProductInstance, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.product} ({self.quantity})'

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def get_cost(self):
        cost = self.product.price * self.quantity
        return cost

    def increment_quantity(self):
        self.quantity += 1
        self.save()



class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_returned = models.BooleanField(null=True)
    request_to_return = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user} - {self.id}'

    def item_list(self):
        return self.items.all()
    
    def can_return(self):
        if timezone.now() - self.created_at > timedelta(minutes=3) or self.is_returned==True:
            return False
        return True

    def request_return(self):
        if not self.can_return():
            return False
        
        self.request_to_return = True
        self.save()
        
        return True

    def return_order(self):
        
        for item in self.items.all():
            product_instance = item.product
            product_instance.quantity += item.quantity
            product_instance.save()

        user = self.user
        user.money += self.total_cost
        user.save()
        
        self.is_returned = True
        self.save()



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProductInstance, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    item_total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.product} ({self.quantity})'
    
    def get_cost(self):
        cost = self.product.price * self.quantity
        return cost



