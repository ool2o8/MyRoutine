import factory
from factory import fuzzy, SubFactory
from .models import Routine, RoutineDay, RoutineResult
from faker import Faker
from accounts.factories import UserFactory

fake = Faker()
fake_ko = Faker('ko_KR')


class RoutineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Routine
    account = SubFactory(UserFactory)
    title = fake.text(max_nb_chars=20)
    category = "HOMEWORK"
    goal = fake.text(max_nb_chars=20)
    is_alarm = "True"


class RoutineDayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RoutineDay

    routine = SubFactory(RoutineFactory)
    day = fuzzy.FuzzyChoice(
        choices=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])


class RoutineResultFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RoutineResult

    routine = SubFactory(RoutineFactory)
    result = fuzzy.FuzzyChoice(choices=['NOT', 'TRY', 'DONE'])
