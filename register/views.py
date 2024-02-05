from django.shortcuts import render, redirect
from register.forms import RegisterForm
from django.views import View
from django.contrib.auth import login, logout, authenticate
def register(response):
    if response.method =='POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = RegisterForm()

    return render(response, 'register/register.html', {"form": form})

def logout_view(request):
    logout(request)
    return redirect('index')