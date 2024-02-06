"""
URL configuration for EatNow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from customer.views import Index, About, Restaurant, JoinUs, Order, OrderConfirmation, OrderPayConfirmation, Menu, MenuSearch, RestaurantSearch, RestaurantMenuView, Cart
from django.conf.urls.static import static
from django.conf import settings
from register import views as v



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





