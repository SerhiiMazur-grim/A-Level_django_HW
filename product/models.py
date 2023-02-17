from django.db import models
import uuid
from django.template.defaultfilters import slugify


class Category(models.Model):
    category = models.CharField('Category', max_length=50)
    
    def __str__(self) -> str:
        return self.category


class ProductInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    title = models.CharField(max_length=150, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.FloatField(default=0.0)
    count = models.IntegerField(default=0)
    added = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    