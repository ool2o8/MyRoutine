# Generated by Django 4.1.4 on 2022-12-08 05:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('기상', 'MIRACLE'), ('숙제', 'HOMEWORK')], max_length=10)),
                ('goal', models.CharField(max_length=200)),
                ('is_alarm', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 8, 14, 50, 27, 975817))),
                ('modified_at', models.DateTimeField(null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routines', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoutineResult',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('result', models.CharField(choices=[('NOT', 'NOT'), ('TRY', 'TRY'), ('DONE', 'DONE')], default='NOT', max_length=4)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 8, 14, 50, 27, 976786))),
                ('modified_at', models.DateTimeField(null=True)),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='routine.routine')),
            ],
        ),
        migrations.CreateModel(
            name='RoutineDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('MON', 0), ('TUE', 1), ('WED', 2), ('THU', 3), ('FRI', 4), ('SAT', 5), ('SUN', 6)], max_length=3)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 8, 14, 50, 27, 976786))),
                ('modified_at', models.DateTimeField(null=True)),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day', to='routine.routine')),
            ],
        ),
    ]
