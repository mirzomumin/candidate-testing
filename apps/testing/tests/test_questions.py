from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

from user.tests.user_factory import UserFactory
from .factories.question import QuestionFactory
from .factories.test import TestFactory


class TestView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user.tokens()['access'])
        self.test = TestFactory()
        self.questions = QuestionFactory.create_batch(10, test=self.test)
        self.questions_url = reverse('testing:vacancy_test', args=[self.test.id])

    def test_questions(self):
        response = self.client.get(self.questions_url)
        self.assertEqual(response.status_code, 200)
        for i, q in enumerate(self.questions):
            self.assertEqual(response.data[i]['title'], q.title)
