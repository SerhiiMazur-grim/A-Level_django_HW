from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'username',
                'placeholder': "Username"
                }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': "password",
                'placeholder': "Password",
                })
        }
    
class UserRegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': "confirmPassword",
                'placeholder': "Confirm Password",
                }))
    
    class Meta:
        model = User
        
        fields = [
            'username',
            'email',
            'password',
        ] 
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'username',
                'placeholder': "Username"
                }),
            
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder':'Enter E-Mail'
                }),
            
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': "password",
                'placeholder': "Password",
                }),
        }
