from .models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError
import re


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(
        max_length=50, help_text='특수문자, 숫자를 포함한 8글자 이상')

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise ValidationError("이미 사용중인 이메일 입니다.")
        return email

    def validate_password(self, password):
        PASSWORD_VALIDATION = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
        if not re.match(PASSWORD_VALIDATION, password):
            raise ValidationError(
                "비밀번호는 8글자 이상이며 특수문자($@$!%*#?&), 숫자를 포함해야 합니다.")
        return password


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
