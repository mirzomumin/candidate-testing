from rest_framework.test import APITestCase
from django.urls import reverse

from user.tests.user_factory import UserFactory
from .factories.test import TestFactory


class TestView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user.tokens()['access'])
        self.test = TestFactory()
        self.test_info_url = reverse('testing:test_info', args=[self.test.id])

    def test_info(self):
        response = self.client.get(self.test_info_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], self.test.title)
