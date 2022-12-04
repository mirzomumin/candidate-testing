from rest_framework.test import APITestCase
from django.urls import reverse

from .factories.category import CategoryFactory

class TestView(APITestCase):

    def setUp(self):
        self.categories = CategoryFactory()
        self.categories_url = reverse('vacancy:categories')

    def test_category(self):
        response = self.client.get(self.categories_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], self.categories.name)