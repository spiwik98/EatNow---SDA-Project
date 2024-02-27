from django.urls import path
from customer import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('order/', views.Order.as_view(), name='order'),
    path('', views.Index.as_view(), name='base'),
    path('about/', views.About.as_view(), name='about'),
    path('joinus/', views.JoinUs.as_view(), name='joinus'),
    path('order-confirmation/<int:pk>', views.OrderConfirmation.as_view(), name='order-confirmation'),
    path('payment-confirmation/', views.OrderPayConfirmation.as_view(), name='payment-submitted'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('menu/search/', views.MenuSearch.as_view(), name='menu-search'),
    path('restaurants/', views.Restaurants.as_view(), name='restaurants'),
    path('restaurants/<int:restaurant_id>/', views.RestaurantMenuView.as_view(), name='restaurants_menu'),
    path('restaurant/search/', views.RestaurantSearch.as_view(), name='cuisine-type-search'),
    path('cart/', views.Cart.as_view(), name='cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
