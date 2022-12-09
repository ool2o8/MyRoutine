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



fake = Faker()
fake_ko = Faker('ko_KR')


class RoutineTests(APITestCase):
    urlpatterns = [
        path('routines/', include('routine.urls')),
    ]

    def setUp(self):
        self.client = APIClient()
        self.user=User.objects.create(
            email="ncr7804@naver.com",
            username="ool2o8",
        )
        self.user.set_password('mijung1208!')
        self.user.save()

    def test_create_routine(self):
        url = reverse('routine-routines')
        self.client.login(email='ncr7804@naver.com', password='mijung1208!')
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

    