from faker import Faker
from unittest.mock import patch
from rest_framework.test import APIClient
import string
import random
import factory.fuzzy
from django.test import Client
from django.test.testcases import TestCase
from rest_framework.test import APITestCase
from accounts.factories import UserFactory
from django.urls import path, include, reverse
from rest_framework.test import force_authenticate, APIRequestFactory
from accounts.models import User
from .factories import RoutineFactory
from .models import Routine, RoutineDay, RoutineResult



fake = Faker()
fake_ko = Faker('ko_KR')


class RoutineCreateTests(APITestCase):
    urlpatterns = [
        path('routines', include('routine.urls')),
    ]

    def setUp(self):
        self.client = APIClient()
        self.user=User.objects.create(
            email="ncr7804@naver.com",
            username="ool2o8",
        )
        self.user.set_password('mijung1208!')
        self.user.save()
        self.client.login(email='ncr7804@naver.com', password='mijung1208!')

    def test_create_routine(self):
        url = reverse('routine-create')
        
        data = {
            "title":fake.sentence(),
            "category":"HOMEWORK",
            "goal":fake.sentence(),
            "is_alarm":"true",
            "days":["MON", "TUE"]
        }
        print(data)

        response = self.client.post(url, data, format='json')
        print(response)
        print(response.status_code)


class AfterRoutineCreateTest(APIClient):
    urlpatterns = [
        path('routines', include('routine.urls')),
    ]

    def setUp(self):
        self.client = APIClient()
        user=User.objects.create(
            email="ncr7804@naver.com",
            username="ool2o8",
        )
        user.set_password('mijung1208!')
        user.save()
        self.client.login(email='ncr7804@naver.com', password='mijung1208!')
        routine=Routine.objects.create(
            title="problem solving5",
            category="HOMEWORK",
            goal="goal",
            is_alarm="true",
            days=["MON", "SAT"]
        )
        

    def test_routine_update(self):
        url = 'routines/1/update'
        routine=RoutineFactory()
        data = {
            "routine":routine.id,
            "title":"problem solving5",
            "category":"HOMEWORK",
            "goal":"goal",
            "is_alarm":"true",
            "days":["MON", "FRI"]
        }
        print(data)

        response = self.client.put(url, data, format='json')
        print(response)
        print(response.status_code)

    def test_routine_list(self):
        url = reverse('routine-list')

        response = self.client.get(url,format='json')
        print(response['data'])
        print(response.status_code)

    