import factory, string, random
from factory import fuzzy, SubFactory
from .models import Routine, RoutineDay, RoutineResult
from faker import Faker
from assignment.accounts.factories import UserFactory

fake = Faker()
fake_ko = Faker('ko_KR')


class RoutineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Routine

    account=SubFactory(UserFactory())


class RoutineDayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Routine

    routine=SubFactory(RoutineFactory)
    day=fuzzy.FuzzyChoice(choices=['MON', 'TUE', 'WED','THU','FRI','SAT','SUN'])





