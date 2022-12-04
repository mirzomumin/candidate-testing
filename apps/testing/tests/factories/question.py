import factory
from faker import Faker

from testing.models import Question
from .test import TestFactory

faker = Faker()


class QuestionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Question

    test = factory.SubFactory(TestFactory)
    title = faker.name()
    point = 2