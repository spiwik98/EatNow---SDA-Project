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
from django.urls import path
from customer.views import Index, About, Restaurant, LogInCreateAccount, JoinUs, Order
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', Order.as_view(), name='order'),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('restaurant/', Restaurant.as_view(), name='restaurant'),
    path('login/', LogInCreateAccount.as_view(), name='login'),
    path('joinus/', JoinUs.as_view(), name='joinus'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
