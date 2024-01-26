from django.shortcuts import render
from django.views import View


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')


class Restaurant(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/restaurant.html')


class LogInCreateAccount(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/login.html')

class JoinUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/joinus.html')

