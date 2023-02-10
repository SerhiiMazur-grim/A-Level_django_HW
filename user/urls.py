from django.urls import path
from user.views import signin, signup, user_logout


urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
]

