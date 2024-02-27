from django.contrib import admin
from .models import MenuItem, Category, OrderModel, Restaurant, CuisineType


admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderModel)
admin.site.register(Restaurant)
admin.site.register(CuisineType)
