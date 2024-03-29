# Generated by Django 4.0.6 on 2023-05-09 13:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0044_alter_task_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('491e8de6-e5f9-470b-9fd6-3b3222814241'), editable=False, unique=True),
        ),
    ]
