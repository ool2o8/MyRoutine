from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from .serializers import CreateUserSerializer, LoginSerializer
from .models import User
from django.contrib.auth import authenticate, login, logout


class CreateUser(viewsets.ModelViewSet):
    serializer_class = CreateUserSerializer

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                user = User.objects.create_user(
                    username=request.POST['username'],
                    email=request.POST['email'],
                    password=request.POST['password']
                )
                return Response("UserCreate complete", status=status.HTTP_201_CREATED)
        except:
            return Response("Validation error", status=status.HTTP_400_BAD_REQUEST)


class Login(viewsets.ModelViewSet):
    serializer_class = LoginSerializer

    def post(self, request):
        user = authenticate(
            request, email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return Response("로그인 성공", status=status.HTTP_200_OK)
        else:
            return Response("로그인에 실패하였습니다.", ststus=status.HTTP_400_BAD_REQUEST)


class Logout(viewsets.ModelViewSet):
    def get(self, request):
        logout(request)
        return Response("로그아웃", status=status.HTTP_200_OK)
