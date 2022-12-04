from rest_framework.test import APITestCase
from django.urls import reverse

from user.tests.user_factory import UserFactory
from .factories.category import CategoryFactory
from .factories.vacancy import VacancyFactory
from testing.tests.factories.test import TestFactory
from testing.tests.factories.user_response import UserResponseFactory
from testing.tests.factories.question import QuestionFactory


class TestView(APITestCase):

    def setUp(self):
        self.test = TestFactory()
        self.category = CategoryFactory()
        self.vacancy = VacancyFactory(category=self.category, test=self.test)
        self.user = UserFactory.create(vacancies=(self.vacancy,))
        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + self.user.tokens()['access'])
        self.user_response = UserResponseFactory(user=self.user, test=self.test)
        self.question = QuestionFactory.create_batch(5, test=self.test)
        self.url = reverse('vacancy:vacancies_applied')
        
        

    def test_vacancies_applied(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], self.vacancy.title)