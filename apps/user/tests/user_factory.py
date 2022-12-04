import factory
from faker import Faker

from user.models import CustomUser


faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser
        django_get_or_create = ('email',)

    email = faker.email()
    username = faker.first_name()
    last_name = faker.last_name()
    phone = faker.phone_number()
    
    @factory.post_generation
    def vacancies(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for vacancy in extracted:
                self.vacancies.add(vacancy)