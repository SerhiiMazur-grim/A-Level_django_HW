from django.urls import path
from .views import MyLoginView, MyRegister, MyLogout


urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('register/', MyRegister.as_view(), name='register'),
    path('logout/', MyLogout.as_view(), name='logout'),
]
