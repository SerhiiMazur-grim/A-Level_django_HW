from django.db import models


class Category(models.Model):
    category = models.CharField('Category', max_length=50)
    
    def __str__(self) -> str:
        return self.category

class Article(models.Model):
    title = models.CharField('Title', max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField('Content')
    added = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return self.title