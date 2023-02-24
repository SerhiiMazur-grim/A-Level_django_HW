from django.urls import path

from .views import (
    home_page,
    article_page,
    article_by_category,
    ArticleListAPIView,
    ArticleDetailAPIView,
    ArticleCreateAPIView,
    ArticleUpdateAPIView,
    ArticleDeleteAPIView,
)

urlpatterns = [
    path('homepage/', home_page, name='home'),
    path('home/', home_page, name='home'),
    path('', home_page, name='home'),
    path('article/<int:id>/', article_page, name='article_page'),
    path('category/<str:select_category>/', article_by_category, name='article_by_category'),
    
    path('articles/', ArticleListAPIView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article_detail'),
    path('articles/create/', ArticleCreateAPIView.as_view(), name='article_create'),
    path('articles/<int:pk>/update/', ArticleUpdateAPIView.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', ArticleDeleteAPIView.as_view(), name='article_delete'),
]