from django.contrib import admin
from django.urls import path, include

from .views import RoutineCreateView, RoutineListView, RoutineView
urlpatterns = [
    path('routines', RoutineCreateView.as_view()),
    path('routines/<int:pk>',RoutineView.as_view({"get":"get","put":"put", "delete":"delete"})),
    path('list', RoutineListView.as_view())
    
]