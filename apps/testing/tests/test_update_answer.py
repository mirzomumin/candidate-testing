from rest_framework.test import APITestCase
from django.urls import reverse

from user.tests.user_factory import UserFactory
from .factories.option import OptionFactory
from .factories.question import QuestionFactory
from .factories.test import TestFactory
from .factories.user_response import UserResponseFactory
from .factories.answer import AnswerFactory


class TestView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user.tokens()['access'])
        self.test = TestFactory()
        self.question = QuestionFactory(test=self.test)
        self.option = OptionFactory(question=self.question)
        self.user_response = UserResponseFactory(user=self.user, test=self.test)
        self.answer = AnswerFactory(response=self.user_response, question=self.question, option=self.option)
        self.update_answer_url = reverse('testing:update_answer')
    
    def test_create_answer(self):
        data = {
            "response": self.answer.response.id,
            "question": self.answer.question.id,
            "option": self.answer.option.id
        }
        response = self.client.patch(self.update_answer_url, data, format='json')
        
        self.assertEqual(response.status_code, 201)