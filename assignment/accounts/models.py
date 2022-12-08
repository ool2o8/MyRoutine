from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
