# Generated by Django 4.0.6 on 2023-02-12 15:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0023_alter_task_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('b4a71968-d39b-4f3f-93c6-9e6a250edddc'), editable=False, unique=True),
        ),
    ]
