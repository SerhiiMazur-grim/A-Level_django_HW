from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from product.models import Category
from .forms import Log_in, CustomUserCreationForm


class MyLoginView(LoginView):
    form_class = Log_in
    success_url = reverse_lazy('home')
    template_name = 'user/login.html'
    
    def get_success_url(self):
        return self.success_url


class MyRegister(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user/register.html'
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data.get('email')
        user.save()
        return super().form_valid(form)


class MyLogout(LogoutView):
    next_page = reverse_lazy('home')

    def get_next_page(self):
        return self.next_page
