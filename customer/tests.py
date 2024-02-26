# Importujemy niezbędne moduły
import pytest
from django.contrib.auth.models import User
from customer.models import MenuItem, Category, OrderModel, CuisineType, RestaurantName, Profile


# Test jednostkowy dla MenuItem
@pytest.mark.django_db
def test_menu_item():
    # Tworzymy obiekty potrzebne do testu
    restaurant = RestaurantName.objects.create(name="Restaurant 1")
    category = Category.objects.create(name="Category 1")

    # Tworzymy MenuItem i dodajemy kategorię
    menu_item = MenuItem.objects.create(name="Item 1", description="Description", price=10.99, restaurant=restaurant)
    menu_item.category.add(category)

    # Sprawdzamy, czy dane zostały poprawnie zapisane
    assert menu_item.name == "Item 1"
    assert menu_item.description == "Description"
    assert menu_item.price == 10.99
    assert menu_item.restaurant == restaurant
    assert menu_item.category.count() == 1


# Test jednostkowy dla OrderModel
@pytest.mark.django_db
def test_order_model():
    # Tworzymy obiekt OrderModel
    order = OrderModel.objects.create(price=20.50, name="John Doe", email="john@example.com")

    # Sprawdzamy, czy dane zostały poprawnie zapisane
    assert order.price == 20.50
    assert order.name == "John Doe"
    assert order.email == "john@example.com"


# Test jednostkowy dla CuisineType
@pytest.mark.django_db
def test_cuisine_type():
    # Tworzymy obiekt CuisineType
    cuisine_type = CuisineType.objects.create(name="Italian")

    # Sprawdzamy, czy dane zostały poprawnie zapisane
    assert cuisine_type.name == "Italian"


# Test jednostkowy dla RestaurantName
@pytest.mark.django_db
def test_restaurant_name():
    # Tworzymy obiekty potrzebne do testu
    cuisine_type = CuisineType.objects.create(name="Italian")

    # Tworzymy obiekt RestaurantName
    restaurant = RestaurantName.objects.create(name="Restaurant 1", type=cuisine_type, address="Address 1")

    # Sprawdzamy, czy dane zostały poprawnie zapisane
    assert restaurant.name == "Restaurant 1"
    assert restaurant.type == cuisine_type
    assert restaurant.address == "Address 1"


# Test jednostkowy dla Profile
@pytest.mark.django_db
def test_profile():
    # Tworzymy obiekt User i Profile
    user = User.objects.create_user(username="testuser", email="test@example.com", password="password")
    profile = Profile.objects.create(user=user, name="Test User")

    # Sprawdzamy, czy dane zostały poprawnie zapisane
    assert profile.user.username == "testuser"
    assert profile.name == "Test User"