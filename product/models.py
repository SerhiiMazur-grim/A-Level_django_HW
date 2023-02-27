from django.db import models
import uuid
from django.utils.text import slugify


class Category(models.Model):
    
    """
    A model class representing an instance of a category.
    """
    
    category = models.CharField('Category', max_length=50)

    def __str__(self):
        return self.category


class ProductInstance(models.Model):
    
    """
    A model class representing an instance of a product.
    """
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title
    
    def decrease_quantity(self, quantity_to_decrease=1):
        
        """
        Decreases the quantity of the product instance by a specified amount.
        """
    
        if self.quantity >= quantity_to_decrease:
            self.quantity -= quantity_to_decrease
            self.save()
            return True
        return False

    def save(self, *args, **kwargs):
        
        """
        Overrides the save method to automatically generate a slug for the 
        product instance if one is not provided.
        """
        
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
