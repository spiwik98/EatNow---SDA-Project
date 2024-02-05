from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')
    restaurant = models.ForeignKey('RestaurantName', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField('MenuItem', related_name='order', blank=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=15, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)


    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'

class CuisineType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RestaurantName(models.Model):
    name = models.CharField(max_length=255, blank=True)
    type = models.ForeignKey('CuisineType', on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='restaurant_images/', blank=True)

    def __str__(self):
        return self.name



""" class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    contact = models.IntegerField()
    points = models.IntegerField()


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    date = models.DateField()


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_price = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ImageField(upload_to='menu_images')


class ProductOrder(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class CuisineType(models.Model):
    id = models.AutoField(primary_key=True)
    cuisine_type_name = models.CharField(max_length=255)


    
class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    rate = models.DecimalFielfrom django.contrib import admind(max_digits=5, decimal_places=2)"""



