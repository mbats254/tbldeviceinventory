# Generated by Django 4.0.6 on 2023-05-05 09:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0041_alter_task_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('9c67d686-a086-4602-8bfc-2a164afa75d0'), editable=False, unique=True),
        ),
    ]
