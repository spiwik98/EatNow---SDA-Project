from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User
from django import forms

# Definicja formularza rejestracyjnego
class RegisterForm(UserCreationForm):
    # Dodanie pola e-mail
    email = forms.EmailField()

    class Meta:
        model = User
        # Określenie pól, które będą widoczne w formularzu i ich kolejności
        fields = ['email', 'username', 'password1', 'password2']
