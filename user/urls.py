from django.urls import path
from .views import MyLoginView, MyRegister, user_logout


urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('register/', MyRegister.as_view(), name='register'),
    path('logout/', user_logout, name='logout'),
]
