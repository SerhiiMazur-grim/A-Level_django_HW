from django.shortcuts import redirect
from django.contrib.auth import logout
from product.models import Category
from .forms import Log_in, CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class MyLoginView(LoginView):
    form_class = Log_in
    next_page = 'home'
    extra_context = {'categories': Category.objects.order_by('id'),}
    template_name = 'user/login.html'




class MyRegister(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    extra_context = {'categories': Category.objects.order_by('id'),}
    template_name = 'user/register.html'

def user_logout(request):
    """
    Logout user
    """
    logout(request)
    return redirect('login')
