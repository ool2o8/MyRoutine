from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import LoginSerializer, SignUpSerializer
from .models import User
from django.contrib.auth import authenticate, login, logout



class SignUpView(viewsets.ModelViewSet):
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.create_user(
                username=serializer.data['username'],
                email=serializer.data['email'],
                password=serializer.data['password']
            )
            return Response("UserCreate complete", status=status.HTTP_201_CREATED)
        return Response("Validation error", status=status.HTTP_400_BAD_REQUEST)


class LoginView(viewsets.ModelViewSet):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(request.data)
        email = serializer.data['email']
        password = serializer.data['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return Response("로그인 성공", status=status.HTTP_200_OK)
        return Response("로그인에 실패하였습니다.", status=status.HTTP_400_BAD_REQUEST)


class LogoutView(viewsets.ModelViewSet):
    def get(self, request):
        logout(request)
        return Response("로그아웃", status=status.HTTP_200_OK)
