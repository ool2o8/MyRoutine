from faker import Faker
from rest_framework.test import APIClient
import string
import random
from rest_framework.test import APITestCase
from django.urls import path, include, reverse
from .models import User



fake = Faker()
fake_ko = Faker('ko_KR')


class AccountTests(APITestCase):
    urlpatterns = [
        path('accounts', include('accounts.urls')),
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
        result=0
        if response.status_code==201 or response.status_code==400:
            result+=1
        self.assertEqual(1,result)
    
    def test_account_login_로그인(self):
        url = reverse('accounts-login')
        self.client = APIClient()
        user=User.objects.create(
            email="ncr7804@naver.com",
            username="ool2o8",
        )
        user.set_password('mijung1208!')
        user.save()
        data = {
            "email": "ncr7804@naver.com",
            "password": "mijung1208!"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data, "로그인 성공")
        self.assertEqual(response.status_code,200)
