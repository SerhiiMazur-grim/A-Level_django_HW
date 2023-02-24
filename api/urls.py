from django.urls import path

from .views import (
    ArticleListAPIView,
    ArticleDetailAPIView,
    ArticleCreateAPIView,
    ArticleUpdateAPIView,
    ArticleDeleteAPIView,
)


urlpatterns = [
    path('api/articles/', ArticleListAPIView.as_view(), name='article_list'),
    path('api/articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article_detail'),
    path('api/articles/create/', ArticleCreateAPIView.as_view(), name='article_create'),
    path('api/articles/<int:pk>/update/', ArticleUpdateAPIView.as_view(), name='article_update'),
    path('api/articles/<int:pk>/delete/', ArticleDeleteAPIView.as_view(), name='article_delete'),
]