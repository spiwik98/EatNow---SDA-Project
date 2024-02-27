from django.test import TestCase
from customer.models import MenuItem, OrderModel, CuisineType, Restaurant, Category


class YourModelTestCase(TestCase):
    def test_menu_item(self):
        restaurant = Restaurant.objects.create(name="Restaurant 1")
        category = Category.objects.create(name="Category 1")
        menu_item = MenuItem.objects.create(name="Item 1",
                                            description="Description", price=10.99, restaurant=restaurant)
        menu_item.category.add(category)
        self.assertEqual(menu_item.name, "Item 1")
        self.assertEqual(menu_item.description, "Description")
        self.assertEqual(menu_item.price, 10.99)
        self.assertEqual(menu_item.restaurant, restaurant)
        self.assertEqual(menu_item.category.count(), 1)

    def test_order_model(self):
        order = OrderModel.objects.create(price=20.50, name="John Doe", email="john@example.com")
        self.assertEqual(order.price, 20.50)
        self.assertEqual(order.name, "John Doe")
        self.assertEqual(order.email, "john@example.com")

    def test_cuisine_type(self):
        cuisine_type = CuisineType.objects.create(name="Italian")
        self.assertEqual(cuisine_type.name, "Italian")

    def test_restaurant(self):
        cuisine_type = CuisineType.objects.create(name="Italian")
        restaurant = Restaurant.objects.create(name="Restaurant 1", type=cuisine_type, address="Address 1")
        self.assertEqual(restaurant.name, "Restaurant 1")
        self.assertEqual(restaurant.type, cuisine_type)
        self.assertEqual(restaurant.address, "Address 1")
