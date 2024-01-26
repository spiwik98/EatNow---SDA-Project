from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
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
    images = models.CharField(max_length=255)


class ProductOrder(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class CuisineType(models.Model):
    id = models.AutoField(primary_key=True)
    cuisine_type_name = models.CharField(max_length=255)


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=255)
    cuisine_type = models.ForeignKey(CuisineType, on_delete=models.CASCADE)
    restaurant_address = models.CharField(max_length=255)
    restaurant_website = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    rate = models.IntegerField()
