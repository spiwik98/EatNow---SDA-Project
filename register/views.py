from django.shortcuts import render, redirect
from register.forms import RegisterForm
from django.contrib.auth import logout


def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = RegisterForm()

    return render(response, 'register/register.html', {"form": form})


def logout_view(request):
    logout(request)
    return redirect('base')
