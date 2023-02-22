from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email", widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Email'
        }))
    first_name = forms.CharField(required=True, label="First Name", widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'First Name'
        }))
    last_name = forms.CharField(required=True, label="Last Name", widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Last Name'
        }))
    password1 = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control', 
        'type': 'password', 
        'placeholder': 'Password'
        }))
    password2 = forms.CharField(required=True, label="Confirm Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control', 
        'type': 'password', 
        'placeholder': 'Confirm Password'
        }))

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2',)



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',)


class Log_in(AuthenticationForm):
    username = forms.EmailField(label='Enter email', widget=forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder':'Enter E-Mail'
                }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': "password",
                'placeholder': "Password",
                }))
    class Meta:
        model = CustomUser
