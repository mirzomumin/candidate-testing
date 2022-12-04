from rest_framework.test import APITestCase
from django.urls import reverse

from user.tests.user_factory import UserFactory
from .factories.test import TestFactory
from vacancy.tests.factories.category import CategoryFactory
from vacancy.tests.factories.vacancy import VacancyFactory

class TestView(APITestCase):

    def setUp(self):
        self.test = TestFactory()
        self.category = CategoryFactory()
        self.vacancy = VacancyFactory(category=self.category, test=self.test)
        self.user = UserFactory.create(vacancies=(self.vacancy,))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user.tokens()['access'])
        self.url = reverse('testing:start_test', args=[self.test.id])
    
    def test_create_answer(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['data']['test'], self.test.id)