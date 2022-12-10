# Generated by Django 4.1.4 on 2022-12-10 09:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0003_alter_routine_created_at_alter_routineday_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 10, 18, 12, 11, 871480)),
        ),
        migrations.AlterField(
            model_name='routineday',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 10, 18, 12, 11, 871480)),
        ),
        migrations.AlterField(
            model_name='routineday',
            name='routine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='routine.routine'),
        ),
        migrations.AlterField(
            model_name='routineresult',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 10, 18, 12, 11, 871480)),
        ),
    ]