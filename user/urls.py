from django.urls import path
from user.views import log_in, reg_user


urlpatterns = [
    path('login/', log_in, name='login'),
    path('regitration/', reg_user, name='regitration'),
]
