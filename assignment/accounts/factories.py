import factory
from .models import User
from faker import Faker

fake = Faker()
fake_ko = Faker('ko_KR')


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = fake.email()
    username = fake.user_name()
    password = fake.password()
