# Generated by Django 4.0.2 on 2022-06-03 18:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0002_alter_task_uniqid_alter_taskmonitor_resourceuniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('5f181082-0b8b-4738-90c8-ba7f99d88882'), editable=False, unique=True),
        ),
    ]
