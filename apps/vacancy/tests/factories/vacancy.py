import factory
from faker import Faker

from vacancy.models import  Vacancy
from .category import CategoryFactory
from testing.tests.factories.test import TestFactory


faker = Faker()


class VacancyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vacancy

    category = factory.SubFactory(CategoryFactory)
    test = factory.SubFactory(TestFactory)
    title = faker.company()
    company_name = faker.company()
    short_description = faker.company()
    duties = faker.text()
    requirements = faker.text()
    offers = faker.text()
    contact_person = faker.name()
    phone = faker.phone_number()
    email = faker.ascii_company_email()
    address = faker.url()
    website = faker.url()
    is_active = True