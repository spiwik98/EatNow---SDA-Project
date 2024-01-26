from django.contrib import admin

from customer.models import Profile, Order, Product, ProductOrder, CuisineType, Restaurant, Rating


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class ProductOrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductOrder, ProductOrderAdmin)


class CuisineTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(CuisineType, CuisineTypeAdmin)


class RestaurantAdmin(admin.ModelAdmin):
    pass


admin.site.register(Restaurant, RestaurantAdmin)


class RatingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Rating, RatingAdmin)