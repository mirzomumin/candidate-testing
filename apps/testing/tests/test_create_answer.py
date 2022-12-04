from rest_framework.test import APITestCase
from django.urls import reverse

from user.tests.user_factory import UserFactory
from .factories.option import OptionFactory
from .factories.question import QuestionFactory
from .factories.test import TestFactory
from .factories.user_response import UserResponseFactory


class TestView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user.tokens()['access'])
        self.test = TestFactory()
        self.question = QuestionFactory(test=self.test)
        self.option = OptionFactory(question=self.question)
        self.user_response = UserResponseFactory(user=self.user, test=self.test)
        self.create_answer_url = reverse('testing:create_answer')
    
    def test_create_answer(self):
        data = {
            "response": self.user_response.id,
            "question": self.question.id,
            "option": self.option.id
        }
        response = self.client.post(self.create_answer_url, data, format='json')
        
        self.assertEqual(response.status_code, 201)

