from .models import Routine, RoutineDay, RoutineResult
from rest_framework import serializers

class RoutineDaySerializer(serializers.Serializer):
    day=serializers.ChoiceField(choices=[('MON'),('TUE'),('WED'),('THU'),('FRI'),('SAT'),('SUN'),])


class CreateRoutineSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=50)
    category=serializers.ChoiceField(choices=[('MIRACLE'),('HOMEWORK'),],required=True)
    goal=serializers.CharField(max_length=200)
    is_alarm=serializers.BooleanField(default=False)
    days=serializers.ListSerializer(child=serializers.CharField())


        