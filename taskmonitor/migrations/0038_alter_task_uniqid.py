# Generated by Django 4.0.6 on 2023-03-07 11:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0037_alter_task_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('76ab4b6f-6e14-41ad-a80f-b9eb929bbf6c'), editable=False, unique=True),
        ),
    ]
