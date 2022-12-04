import factory
from vacancy.models import Category
    

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ('name',)

    name = 'Category Title'