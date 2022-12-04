from rest_framework.test import APITestCase
from django.urls import reverse

from user.tests.user_factory import UserFactory
from .factories.option import OptionFactory
from .factories.question import QuestionFactory
from .factories.test import TestFactory
from .factories.answer import AnswerFactory
from .factories.user_response import UserResponseFactory
from vacancy.tests.factories.category import CategoryFactory
from vacancy.tests.factories.vacancy import VacancyFactory

class TestView(APITestCase):

    def setUp(self):
        self.test = TestFactory()
        self.category = CategoryFactory()
        self.vacancy = VacancyFactory(category=self.category, test=self.test)
        self.user = UserFactory.create(vacancies=(self.vacancy,))
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user.tokens()['access'])
        self.question = QuestionFactory(test=self.test)
        self.option = OptionFactory(question=self.question)
        self.user_response = UserResponseFactory(user=self.user, test=self.test, is_ended=False)
        self.answer = AnswerFactory(response=self.user_response, question=self.question, option=self.option)
        self.url = reverse('testing:end_test', args=[self.user_response.id])
    
    def test_create_answer(self):
        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, 200)