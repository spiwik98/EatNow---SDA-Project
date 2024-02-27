from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from register.forms import RegisterForm
from django.contrib.auth import get_user_model


class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/register.html')
        self.assertIsInstance(response.context['form'], RegisterForm)

    def test_register_view_post(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(reverse('register'), data)
        self.assertRedirects(response, reverse('base'))

        # Check if user was created
        self.assertTrue(get_user_model().objects.filter(username='testuser').exists())

    def test_register_view_invalid_form(self):
        data = {}  # Empty data to make form invalid
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/register.html')
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], RegisterForm)
        self.assertFalse(get_user_model().objects.filter(username='testuser').exists())  # Make sure user wasn't created


class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('base'))
        self.assertFalse(response.wsgi_request.user.is_authenticated)