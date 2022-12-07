from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import CreateUserSerializer, LoginSerializer
from .models import User
from django.contrib.auth import authenticate, login, logout


class CreateUser(viewsets.ModelViewSet):
    serializer_class=CreateUserSerializer
    def post(self, request):
        serializer=CreateUserSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response("Valid error", status=status.HTTP_400_BAD_REQUEST)
        else:
            user = User.objects.create_user(
                username = request.POST['username'],
                email = request.POST['email'],
                password=request.POST['password']
            )
            return Response("UserCreate complete", status=status.HTTP_201_CREATED)


class Login(viewsets.ModelViewSet):
    serializer_class=LoginSerializer
    def post(self, request):
        user=authenticate(request, email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return Response("로그인 성공", status=status.HTTP_200_OK)
        else:
            return Response("로그인에 실패하였습니다.", ststus=status.HTTP_401_UNAUTHORIZED)


class Logout(viewsets.ModelViewSet):
    def get(self, request):
        logout(request)
        return Response("로그아웃", status=status.HTTP_200_OK)