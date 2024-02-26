# Importowanie wymaganych modułów
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from customer.views import Index, About, Restaurant, JoinUs, Order, OrderConfirmation, OrderPayConfirmation, Menu, MenuSearch, RestaurantSearch, RestaurantMenuView, Cart
from register import views as v

# Lista URLi
urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', Order.as_view(), name='order'),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('joinus/', JoinUs.as_view(), name='joinus'),
    path('order-confirmation/<int:pk>', OrderConfirmation.as_view(), name='order-confirmation'),
    path('payment-confirmation/', OrderPayConfirmation.as_view(), name='payment-submitted'),
    path('menu/', Menu.as_view(), name='menu'),
    path('menu/search/', MenuSearch.as_view(), name='menu-search'),
    path('restaurants/', Restaurant.as_view(), name='restaurants'),
    path('restaurants/<int:restaurant_id>/', RestaurantMenuView.as_view(), name='restaurants_menu'),
    path('restaurant/search/', RestaurantSearch.as_view(), name='cuisine-type-search'),
    path('cart/', Cart.as_view(), name='cart'),
    path('register/', v.register, name='register'),
    path('logout/', v.logout_view, name='logout'),
    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)