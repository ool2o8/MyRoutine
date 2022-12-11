# Generated by Django 4.1.4 on 2022-12-11 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0004_alter_routine_created_at_alter_routineday_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='routine',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='routineday',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='routineday',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='routineresult',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='routineresult',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]