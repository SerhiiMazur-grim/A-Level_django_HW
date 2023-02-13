from django.urls import path
from .views import home


urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('homepage/', home, name='home'),
]
