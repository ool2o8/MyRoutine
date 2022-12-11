from django.db import models
from accounts.models import User


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
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True, null=True)


class RoutineResult(models.Model):
    id=models.BigAutoField(primary_key=True)
    routine=models.OneToOneField(Routine, on_delete=models.CASCADE, related_name='result')
    CHOICE=(
        ('NOT','NOT'),
        ('TRY', 'TRY'),
        ('DONE','DONE')
    )
    result=models.CharField(choices=CHOICE, max_length=4, default='NOT')
    is_deleted=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True, null=True)


class RoutineDay(models.Model):
    CHOICES=(
        ('MON','MON'),
        ('TUE', 'TUE'),
        ('WED','WED'),
        ('THU', 'THU'),
        ('FRI', 'FRI'),
        ('SAT', 'SAT'),
        ('SUN', 'SUN'),
    )
    day=models.CharField(choices=CHOICES, max_length=3)
    routine=models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='days')
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True, null=True)