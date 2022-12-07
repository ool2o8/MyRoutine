from django.db import models
from accounts.models import User
from multiselectfield import MultiSelectField
from datetime import datetime

class Routine(models.Model):
    category_choices=[
        ('기상', 'MIRACLE'),
        ('숙제', 'HOMEWORK'),
    ]
    id=models.BigAutoField(primary_key=True)
    account=models.ForeignKey(User, on_delete=models.CASCADE, related_name='routines')
    title=models.CharField(max_length=50)
    category=models.CharField(max_length=10, choices=category_choices)
    goal=models.CharField(max_length=200)
    is_alarm=models.BooleanField(default=False)
    is_deleted=models.BooleanField(default=False)
    created_at=models.DateTimeField(default=datetime.now())
    modified_at=models.DateTimeField(null=True)

class RoutineResult(models.Model):
    id=models.BigAutoField(primary_key=True)
    routine=models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='result')
    result=models.BooleanField(default=False)
    is_deleted=models.BooleanField(default=False)
    created_at=models.DateTimeField(default=datetime.now())
    modified_at=models.DateTimeField(null=True)

class RoutineDay(models.Model):
    DAY=(
        ('MON', 'monday'),
        ('TUE', 'tuesday'),
        ('WED', 'wednesday'),
        ('THU', 'thursday'),
        ('FRI', 'friday'),
        ('SAT', 'saturday'),
        ('SUN', 'sunday')
    )
    day=models.CharField(choices=DAY,max_length=3)
    routine=models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='day')
    created_at=models.DateTimeField(default=datetime.now())
    modified_at=models.DateTimeField(null=True)