from django.urls import path
from user.views import signin, signup


urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
]

