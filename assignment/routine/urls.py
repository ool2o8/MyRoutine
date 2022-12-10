from django.contrib import admin
from django.urls import path, include

from .views import RoutineCreateView, RoutineListView, RoutineView, RoutineListView
urlpatterns = [
    path('routines', RoutineCreateView.as_view(), name='routine-routines'),
    path('routines/<int:pk>',RoutineView.as_view({"get":"get","put":"put", "delete":"delete"}), name='routine-routines-detail'),
    path('list', RoutineListView.as_view(), name='routine-list')
  
]