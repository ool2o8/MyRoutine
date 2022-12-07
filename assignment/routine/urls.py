from django.contrib import admin
from django.urls import path, include

from .views import CreateRoutine
urlpatterns = [
    path('routine/', CreateRoutine.as_view({'post': 'post'})),
]