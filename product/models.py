from django.db import models


class Category(models.Model):
    category = models.CharField('Category', max_length=50)
    
    def __str__(self) -> str:
        return self.category
