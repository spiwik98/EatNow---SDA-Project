from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from .models import MenuItem, Category, OrderModel, RestaurantName, CuisineType
from django.db.models import Q
from django.shortcuts import render



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
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')



        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

            for item in order_items['items']:
                price += item['price']
                item_ids.append(item['id'])

            order = OrderModel.objects.create(
                price=price,
                name=name,
                email=email,
                street=street,
                city=city,
                state=state,
                zip_code=zip_code)

            order.items.add(*item_ids)

            # After everything is done, send confirmation email to the user
            body = ('Thank you for your order! Your food is being made and will be delivered soon!\n'
                    f'Your total: {price}\n'
                    'Thank you again for your order!')

            send_mail(
                'Thank You For Your Order!',
                body,
                'example@example.com',
                [email],
                fail_silently=False
            )

        context = {
                'items': order_items['items'],
                'price': price,
            }

        return redirect('order-confirmation', pk=order.pk)



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



class Restaurant(View):
    def get(self, request, *args, **kwargs):
        restaurant_items = RestaurantName.objects.all()
        context = {
            'restaurant_items': restaurant_items
        }
        return render(request, 'customer/restaurants.html', context)

class RestaurantSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")
        restaurant_items = RestaurantName.objects.filter(
            Q(type__name__icontains=query) |
            Q(name__icontains=query)
        )
        context = {
            'restaurant_items': restaurant_items,
        }
        return render(request, 'customer/restaurants.html', context)


class RestaurantMenuView(View):
    template_name = 'customer/restaurant_menu.html'

    def get(self, request, restaurant_id, *args, **kwargs):
        restaurant = RestaurantName.objects.get(pk=restaurant_id)

        menu_items = restaurant.menuitem_set.all()
        print(menu_items)
        context = {
            'restaurant': restaurant,
            'menu_items': menu_items,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')



        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

            for item in order_items['items']:
                price += item['price']
                item_ids.append(item['id'])

            order = OrderModel.objects.create(
                price=price,
                name=name,
                email=email,
                street=street,
                city=city,
                state=state,
                zip_code=zip_code)

            order.items.add(*item_ids)

            # After everything is done, send confirmation email to the user
            body = ('Thank you for your order! Your food is being made and will be delivered soon!\n'
                    f'Your total: {price}\n'
                    'Thank you again for your order!')

            send_mail(
                'Thank You For Your Order!',
                body,
                'example@example.com',
                [email],
                fail_silently=False
            )

        context = {
                'items': order_items['items'],
                'price': price,
            }

        return redirect('order-confirmation', pk=order.pk)
