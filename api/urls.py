from django.urls import path, include

from .views import (
    ArticleListAPIView,
    ArticleDetailAPIView,
    ArticleCreateAPIView,
    ArticleUpdateAPIView,
    ArticleDeleteAPIView,
    UserListAPIView,
    UserDetailView,
    UserCreateAPIView,
    UserUpdateAPIView,
    UserDeleteView,
)


urlpatterns = [
    path('api/articles/', ArticleListAPIView.as_view(), name='article_list'),
    path('api/articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article_detail'),
    path('api/articles/create/', ArticleCreateAPIView.as_view(), name='article_create'),
    path('api/articles/<int:pk>/update/', ArticleUpdateAPIView.as_view(), name='article_update'),
    path('api/articles/<int:pk>/delete/', ArticleDeleteAPIView.as_view(), name='article_delete'),
    
    path('api/users/', UserListAPIView.as_view(), name='user_list'),
    path('api/users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('api/users/create/', UserCreateAPIView.as_view(), name='user_create'),
    path('api/users/<int:pk>/update/', UserUpdateAPIView.as_view(), name='user_update'),
    path('api/users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    
    path('api-auth/', include('rest_framework.urls')),
]