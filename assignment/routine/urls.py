from django.contrib import admin
from django.urls import path, include

from .views import RoutineCreateView, RoutineListView, RoutineView, RoutineListView, RoutineUpdateView
urlpatterns = [
    path('', RoutineCreateView.as_view(), name='routine-create'),
    path('/routines', RoutineListView.as_view(), name='routine-list'),
    path('/routines/<int:pk>', RoutineView.as_view(), name='routine-detail'),
    path('/routines/<int:pk>/update', RoutineUpdateView.as_view(), name='routine-update')
    
]