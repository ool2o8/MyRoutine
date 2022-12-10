from .models import Routine, RoutineDay, RoutineResult
from rest_framework import serializers


class CreateRoutineSerializer(serializers.Serializer):
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


class ResultSerialzier(serializers.ModelSerializer):
    class Meta:
        model = RoutineResult
        fields = ['result']


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineDay
        fields = ['day']


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = ['goal', 'account_id', 'title']


class RoutineListSerializer(serializers.ModelSerializer):
    routine = RoutineSerializer()
    class Meta:
        model = RoutineResult
        fields = ['routine', 'result']


class RoutineDetailSerializer(serializers.ModelSerializer):
    day = serializers.ListSerializer(child=DaySerializer(read_only=True))

    class Meta:
        model = Routine
        fields = ['goal', 'account_id', 'title', 'day']


class RoutineRetrieveSerializer(serializers.ModelSerializer):
    routine = RoutineDetailSerializer()

    class Meta:
        model = RoutineResult
        fields = ['routine', 'result']


class roitinelistserializer(serializers.ModelSerializer):
    result=serializers.ResultSerialzier(read_only=True)

    class Meta:
        model=Routine
        fields=[ 'goal', 'account_id', 'result','title']
