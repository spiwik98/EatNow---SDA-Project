from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from .models import MenuItem, Category, OrderModel, RestaurantName
from django.db.models import Q

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class Order(View):
    def get(self, request, *args, **kwargs):
        appetizers = MenuItem.objects.filter(category__name__icontains='Appetizer')
        entres = MenuItem.objects.filter(category__name__icontains='Entre')
        desserts = MenuItem.objects.filter(category__name__icontains='Dessert')
        drinks = MenuItem.objects.filter(category__name__icontains='Drink')

        context = {
            'appetizers': appetizers,
            'entres': entres,
            'desserts': desserts,
            'drinks': drinks,
        }

        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        # Twoja aktualna implementacja dla metody POST
        pass

class OrderConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items.all(),
            'price': order.price,
        }

        return render(request, 'customer/order_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        print(request.body)

class OrderPayConfirmation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/order_pay_confirmation.html')

class Restaurant(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/restaurant.html')

class Restaurants(View):
    def get(self, request, *args, **kwargs):
        restaurant_names = RestaurantName.objects.all()
        context = {
            'restaurant_names': restaurant_names,
        }
        return render(request, 'customer/restaurants.html', context)

class RestaurantsSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")
        restaurant_names = RestaurantName.objects.filter(
            Q(Name__icontains=query)
        )
        context = {
            'restaurant_names': restaurant_names,
        }
        return render(request, 'customer/restaurants.html', context)

    def post(self, request, *args, **kwargs):
        query = self.request.POST.get("q")
        restaurant_names = RestaurantName.objects.filter(
            Q(Name__icontains=query)
        )
        context = {
            'restaurant_names': restaurant_names,
        }
        return render(request, 'customer/restaurants.html', context)

class LogInCreateAccount(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/login.html')

class JoinUs(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/joinus.html')

class Menu(View):
    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()
        context = {
            'menu_items': menu_items,
        }
        return render(request, 'customer/menu.html', context)

class MenuSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")
        menu_items = MenuItem.objects.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query)
        )
        context = {
            'menu_items': menu_items
        }
        return render(request, 'customer/menu.html', context)
