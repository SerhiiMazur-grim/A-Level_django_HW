from django.urls import path

from .views import (
    home_page,
    article_page,
    article_by_category,
)

urlpatterns = [
    path('homepage/', home_page, name='home'),
    path('home/', home_page, name='home'),
    path('', home_page, name='home'),
    path('article/<int:id>/', article_page, name='article_page'),
    path('category/<str:select_category>/', article_by_category, name='article_by_category'),
]