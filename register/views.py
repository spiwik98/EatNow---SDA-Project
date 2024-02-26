from django.shortcuts import render, redirect
from register.forms import RegisterForm
from django.views import View
from django.contrib.auth import login, logout, authenticate

# Widok rejestracji użytkownika
def register(response):
    # Sprawdzenie, czy formularz został przesłany (POST)
    if response.method == 'POST':
        # Utworzenie formularza z danymi z żądania
        form = RegisterForm(response.POST)
        # Sprawdzenie poprawności formularza
        if form.is_valid():
            # Zapisanie użytkownika do bazy danych
            form.save()
            # Przekierowanie na stronę główną po udanej rejestracji
            return redirect("index")
    else:
        # Utworzenie pustego formularza, jeśli żądanie nie było typu POST
        form = RegisterForm()

    # Renderowanie strony rejestracji z formularzem
    return render(response, 'register/register.html', {"form": form})

# Widok wylogowania użytkownika
def logout_view(request):
    # Wylogowanie użytkownika
    logout(request)
    # Przekierowanie na stronę główną po udanym wylogowaniu
    return redirect('index')