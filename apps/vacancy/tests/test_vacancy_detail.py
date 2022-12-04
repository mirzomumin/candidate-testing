from rest_framework.test import APITestCase
from django.urls import reverse

from .factories.category import CategoryFactory
from .factories.vacancy import VacancyFactory

class TestView(APITestCase):

    def setUp(self):
        self.categories = CategoryFactory(name='Django')
        self.vacancy = VacancyFactory(category=self.categories)
        self.vacancy_url = reverse('vacancy:vacancy', args=[self.vacancy.id])

    def test_vacancy_detail(self):
        response = self.client.get(self.vacancy_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], self.vacancy.title)