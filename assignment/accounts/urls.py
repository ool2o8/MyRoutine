from django.contrib import admin
from django.urls import path, include

from .views import LoginView, LogoutView, SignUpView
urlpatterns = [
    path('signup', SignUpView.as_view({'post': 'post'}), name='accounts-signup'),
    path('login', LoginView.as_view({'post': 'post'}), name='accounts-login'),
    path('logout', LogoutView.as_view({'get':'get'}), name='accounts-logout')
]
