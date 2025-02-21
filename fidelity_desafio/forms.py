from django.contrib.auth.forms import UserCreationForm  
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


letters_only = RegexValidator(r'^[a-zA-Zá-úÁ-Ú ]+$', 'O nome só pode conter letras.')

password_validator = RegexValidator(
    r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', 
    'A senha deve conter pelo menos 8 caracteres, 1 número, 1 letra maiúscula e 1 caractere especial.'
)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, label="E-mail")
    
    username = forms.CharField(
        max_length=100, 
        required=True, 
        label="Nome de usuário", 
        validators=[letters_only]  
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput, 
        validators=[password_validator],  
        label="Senha"
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput, 
        label="Confirmar senha"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

