# Generated by Django 4.0.2 on 2022-06-03 18:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('daad3d8c-9785-4341-940c-19c4f5bc9c32'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='taskmonitor',
            name='resourceUniqid',
            field=models.CharField(max_length=70),
        ),
    ]
