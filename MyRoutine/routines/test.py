from faker import Faker
from unittest.mock import patch
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from accounts.factories import UserFactory
from django.urls import path, include, reverse
from .factories import RoutineFactory, RoutineResultFactory, RoutineDayFactory


fake = Faker()
fake_ko = Faker('ko_KR')


class RoutineCreateTests(APITestCase):
    urlpatterns = [
        path('routines', include('routines.urls')),
    ]

    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_create_routine(self):
        url = reverse('routine-create')

        data = {
            "title": fake.text(max_nb_chars=20),
            "category": "HOMEWORK",
            "goal": fake.text(max_nb_chars=20),
            "is_alarm": "true",
            "days": ["MON", "TUE"]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)


class AfterRoutineCreateTests(APITestCase):
    urlpatterns = [
        path('routines', include('routines.urls')),
    ]

    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.client.force_login(self.user)

        self.routine = RoutineFactory(account=self.user)
        self.routine_day = RoutineDayFactory(routine=self.routine)
        self.routine_result = RoutineResultFactory(routine=self.routine)

    def test_routine_수정(self):
        url = reverse('routine-update', kwargs={'pk': self.routine.id})

        data = {
            "title": "problem solving5",
            "category": "HOMEWORK",
            "goal": "goal",
            "is_alarm": "true",
            "days": ["MON"]
        }

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_routine_단건조회(self):
        url = reverse('routine-detail', kwargs={'pk': self.routine.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_routine_삭제(self):
        url = reverse('routine-detail', kwargs={'pk': self.routine.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 204)

    def test_routine_목록조회(self):
        url = reverse('routine-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
