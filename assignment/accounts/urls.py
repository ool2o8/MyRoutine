from django.contrib import admin
from django.urls import path, include

from .views import CreateUser, Login
urlpatterns = [
    path('register/', CreateUser.as_view({'post': 'post'})),
    path('login/', Login.as_view({'post':'post'}))
]