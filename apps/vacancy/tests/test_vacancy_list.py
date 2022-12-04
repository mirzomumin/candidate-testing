from rest_framework.test import APITestCase
from django.urls import reverse

from .factories.category import CategoryFactory
from .factories.vacancy import VacancyFactory


class TestView(APITestCase):

    def setUp(self):
        self.categories = CategoryFactory()
        self.vacancies = VacancyFactory.create_batch(10, category=self.categories)
        self.vacancies_url = reverse('vacancy:vacancies')

    def test_vacancy_list(self):
        response = self.client.get(self.vacancies_url)
        self.assertEqual(response.status_code, 200)
        for i, v in enumerate(self.vacancies):
            self.assertEqual(response.data[i]['title'], v.title)