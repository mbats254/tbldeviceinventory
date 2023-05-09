# Generated by Django 4.0.6 on 2023-02-19 21:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0030_alter_task_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('e47c88fa-3b25-4f87-adb8-db6ce7501434'), editable=False, unique=True),
        ),
    ]
