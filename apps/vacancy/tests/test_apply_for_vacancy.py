from rest_framework.test import APITestCase
from django.urls import reverse

from user.tests.user_factory import UserFactory
from .factories.category import CategoryFactory
from .factories.vacancy import VacancyFactory
from testing.tests.factories.test import TestFactory


class TestView(APITestCase):

    def setUp(self):
        self.test = TestFactory()
        self.category = CategoryFactory()
        self.vacancy = VacancyFactory(category=self.category, test=self.test)
        self.user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + self.user.tokens()['access'])
        self.url = reverse('vacancy:apply_for_vacancy', args=[self.vacancy.id])

    def test_apply_for_vacancy(self):
        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['data']['test'], self.vacancy.test.id)