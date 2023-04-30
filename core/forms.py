from django import forms
from django.forms import ModelForm
from django.core.validators import validate_email
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class UsuarioForm(forms.ModelForm):

class CustomUserCreatioForm(UserCreationForm):
    
    class Meta:
        model = User
        fields= ["username" , "first_name" , "last_name" , "email" , "password1" , "password2"]