from django.contrib.auth import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        required_css_class = 'required'
        fields = ('username', 'password')

        forms.widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',}),
            'password': forms.PasswordInput(attrs={'class': 'form-control',})
        }

class UserRegisterForm(UserCreationForm):
    pass