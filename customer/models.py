from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Model reprezentujący pojedynczą pozycję w menu
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')
    restaurant = models.ForeignKey('RestaurantName', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

# Model reprezentujący kategorię dla pozycji w menu
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menu_images/', blank=True)

    def __str__(self):
        return self.name

# Model reprezentujący pojedyncze zamówienie
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

# Model reprezentujący rodzaj kuchni
class CuisineType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model reprezentujący restaurację
class RestaurantName(models.Model):
    name = models.CharField(max_length=255, blank=True)
    type = models.ForeignKey('CuisineType', on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='restaurant_images/', blank=True)

    def __str__(self):
        return self.name

# Model reprezentujący dodatkowe informacje o użytkowniku
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default='Jan Kowalski (Default)', max_length=200, null=True)
    title = models.CharField(default='This is the default, title change it in profile.', max_length=200, null=True)
    profile_img = models.ImageField(default='media/menu_images/Pizza-2.png', upload_to='media', null=True, blank=True)
    street = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=15, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    contact = models.IntegerField(blank=True)
    email = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"