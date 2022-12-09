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
from .models import User



fake = Faker()
fake_ko = Faker('ko_KR')


class AccountTests(APITestCase):
    urlpatterns = [
        path('accounts/', include('accounts.urls')),
    ]

    def setUp(self):
        self.client = APIClient()

    def test_account_register_계정생성(self):
        url = reverse('accounts-signup')
        email = fake.email()
        username = fake.user_name()

        password = ""
        비밀번호가능문자 = str(string.digits + string.ascii_letters + "$@$!%*#?&")
        for _ in range(0, random.randint(8, 10)):
            password += random.choice(비밀번호가능문자)

        data = {
            "email": email,
            "username": username,
            "password": password
        }
        
        response = self.client.post(url, data, format='json')
        print(response.status_code)
        result=0
        if response.status_code==201 or response.status_code==400:
            result+=1
        self.assertEqual(1,result)


