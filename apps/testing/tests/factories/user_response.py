import factory

from testing.models import UserResponse
from user.tests.user_factory import UserFactory
from .test import TestFactory


class UserResponseFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = UserResponse

    user = factory.SubFactory(UserFactory)
    test = factory.SubFactory(TestFactory)
    is_ended = True
    test_result = 10
