from django.db import models
from django.utils import timezone
from datetime import timedelta

from user.models import CustomUser
from product.models import ProductInstance


class Cart(models.Model):
    
    """
    A model class representing an instance of a cart.
    """
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.user} - {self.id}'
    
    def __len__(self):
        return self.items.count()

    def cart_total_cost(self):
        
        """
        The function calculates the total value of all goods in the basket.
        """
    
        self.total = sum(item.get_cost() for item in self.items.all())
        self.save()
        return self.total



class CartItem(models.Model):
    
    """
    A model class representing an instance of a cart item.
    """
    
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProductInstance, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.product} ({self.quantity})'

    def get_cost(self):
        
        """
        The function calculates the total value of the product relative to its quantity in the basket.
        """
        
        cost = self.product.price * self.quantity
        return cost



class Order(models.Model):
    
    """
    A model class representing an instance of a order.
    """
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_returned = models.BooleanField(null=True)
    request_to_return = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user} - {self.id}'

    def item_list(self):
        
        """
        The function returns the queriseet of products in the order.
        """
        
        return self.items.all()
    
    def can_return(self):
        
        """
        The function checks whether the user can return the order.
        """
        
        if timezone.now() - self.created_at > timedelta(minutes=3) or self.is_returned==True:
            return False
        return True

    def request_return(self):
        
        """
        The function initiates the return process.
        """
        
        if not self.can_return():
            return False
        
        self.request_to_return = True
        self.save()
        
        return True

    def return_order(self):
        
        """
        Function to return the order. 
        The user returns money and the goods are returned to the warehouse.
        """
        
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
    
    """
    A model class representing an instance of a order item.
    """
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProductInstance, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    item_total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.product} ({self.quantity})'
    
    def get_cost(self):
        
        """
        The function calculates the total value of the product relative to its quantity in the order.
        """
        
        cost = self.product.price * self.quantity
        return cost



