import factory

from testing.models import Test


class TestFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Test
        django_get_or_create = ('title',)

    title = 'Test Title'
    duration_time = 25