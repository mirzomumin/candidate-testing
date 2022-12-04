import factory

from testing.models import Option
from .question import QuestionFactory


class OptionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Option
        django_get_or_create = ('title',)
    
    title = 'Option Title'
    question = factory.SubFactory(QuestionFactory)
    