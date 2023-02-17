# from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',)


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


# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Enter Password Again', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('email',)

#     def clean_password2(self):

#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class CreateUser(UserCreationForm):
#     username = forms.CharField(label='Username', min_length=4, max_length=32,
#             widget=forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'id': 'username',
#                 'placeholder': "Username"
#     }))
#     email = forms.EmailField(label='Enter email', widget=forms.EmailInput(attrs={
#                 'class': 'form-control',
#                 'id': 'email',
#                 'placeholder':'Enter E-Mail'
#                 }))
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
#                 'class': 'form-control',
#                 'id': "password",
#                 'placeholder': "Password",
#     }))
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={
#                 'class': 'form-control',
#                 'id': "confirmPassword",
#                 'placeholder': "Confirm Password",
#     }))
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
        