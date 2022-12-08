from django.test import TestCase
from faker import Faker
import factory
from .models import User

fake = Faker()


class UserFactory(factory.Factory):
    class Meta:
        model = User
