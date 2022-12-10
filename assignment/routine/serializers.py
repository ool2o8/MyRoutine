from .models import Routine, RoutineDay, RoutineResult
from rest_framework import serializers
from rest_framework.response import Response


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineDay
        fields = ['day']


class CreateUpdateRoutineSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    category = serializers.ChoiceField(
        choices=[('MIRACLE'), ('HOMEWORK'),], required=True)
    goal = serializers.CharField(max_length=200)
    is_alarm = serializers.BooleanField(default=False)
    CHOICES = (
        ('MON'),
        ('TUE'),
        ('WED'),
        ('THU'),
        ('FRI'),
        ('SAT'),
        ('SUN'),
    )
    days = serializers.ListSerializer(
        child=serializers.ChoiceField(choices=CHOICES))


class RoutineSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='account_id')
    result=serializers.SlugRelatedField(read_only=True, slug_field='result')
    class Meta:
        model=Routine
        fields=['goal', 'id', 'result','title']


class RoutineDetailSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='account_id')
    result=serializers.SlugRelatedField(read_only=True, slug_field='result')
    days = serializers.SlugRelatedField(read_only=True, slug_field='day', many=True)
    class Meta:
        model = Routine
        fields = ['goal', 'id','result', 'title', 'days']


        


