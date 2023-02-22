from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class SignInForm(AuthenticationForm):
    """
    Form to authentication user in sistem
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'username',
                'placeholder': "Username",
                "autofocus": True,
                }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': "password",
                'placeholder': "Password",
                }))


class SignUpForm(UserCreationForm):
    """
    Form to create user in sistem
    """
    username = forms.CharField(label='Username', min_length=4, max_length=32,
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'username',
                'placeholder': "Username"
    }))
    email = forms.EmailField(label='Enter email', widget=forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder':'Enter E-Mail'
                }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': "password",
                'placeholder': "Password",
    }))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': "confirmPassword",
                'placeholder': "Confirm Password",
    }))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
