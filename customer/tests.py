import pytest
from django.contrib.auth.models import User
from customer.models import MenuItem, Category, OrderModel, CuisineType, RestaurantName, Profile


@pytest.mark.django_db
def test_menu_item():
    restaurant = RestaurantName.objects.create(name="Restaurant 1")
    category = Category.objects.create(name="Category 1")
    menu_item = MenuItem.objects.create(name="Item 1", description="Description", price=10.99, restaurant=restaurant)
    menu_item.category.add(category)
    assert menu_item.name == "Item 1"
    assert menu_item.description == "Description"
    assert menu_item.price == 10.99
    assert menu_item.restaurant == restaurant
    assert menu_item.category.count() == 1


@pytest.mark.django_db
def test_order_model():
    order = OrderModel.objects.create(price=20.50, name="John Doe", email="john@example.com")
    assert order.price == 20.50
    assert order.name == "John Doe"
    assert order.email == "john@example.com"


@pytest.mark.django_db
def test_cuisine_type():
    cuisine_type = CuisineType.objects.create(name="Italian")
    assert cuisine_type.name == "Italian"


@pytest.mark.django_db
def test_restaurant_name():
    cuisine_type = CuisineType.objects.create(name="Italian")
    restaurant = RestaurantName.objects.create(name="Restaurant 1", type=cuisine_type, address="Address 1")
    assert restaurant.name == "Restaurant 1"
    assert restaurant.type == cuisine_type
    assert restaurant.address == "Address 1"


@pytest.mark.django_db
def test_profile():
    user = User.objects.create_user(username="testuser", email="test@example.com", password="password")
    profile = Profile.objects.create(user=user, name="Test User")
    assert profile.user.username == "testuser"
    assert profile.name == "Test User"
