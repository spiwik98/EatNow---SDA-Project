from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view_returns_200(self):
        response = self.client.get(reverse('base'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer/base.html')


class AboutViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_about_view_returns_200(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer/about.html')


