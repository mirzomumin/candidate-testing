import factory

from testing.models import Answer
from .question import QuestionFactory
from .option import OptionFactory
from .user_response import UserResponseFactory


class AnswerFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Answer
    
    response = factory.SubFactory(UserResponseFactory)
    question = factory.SubFactory(QuestionFactory)
    option = factory.SubFactory(OptionFactory)
    