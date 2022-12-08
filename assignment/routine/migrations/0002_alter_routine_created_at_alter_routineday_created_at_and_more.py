# Generated by Django 4.1.4 on 2022-12-08 06:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 8, 15, 43, 17, 903379)),
        ),
        migrations.AlterField(
            model_name='routineday',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 8, 15, 43, 17, 904379)),
        ),
        migrations.AlterField(
            model_name='routineday',
            name='day',
            field=models.CharField(choices=[(0, 'MON'), (1, 'TUE'), (2, 'WED'), (3, 'THU'), (4, 'FRI'), (5, 'SAT'), (6, 'SUN')], max_length=3),
        ),
        migrations.AlterField(
            model_name='routineresult',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 8, 15, 43, 17, 904379)),
        ),
    ]
