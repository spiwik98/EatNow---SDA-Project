from django.test import TestCase
from register.forms import RegisterForm


class RegisterFormTestCase(TestCase):

    def test_register_form_valid_data(self):
        form_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_form_missing_email(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_register_form_invalid_email(self):
        form_data = {
            'email': 'invalidemail',
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_register_form_passwords_not_matching(self):
        form_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'differentpassword',
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_register_form_password_too_short(self):
        form_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password1': 'short',
            'password2': 'short',
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)
