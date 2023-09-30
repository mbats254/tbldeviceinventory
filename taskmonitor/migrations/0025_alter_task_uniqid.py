# Generated by Django 4.0.6 on 2023-02-12 16:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0024_alter_task_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('d5a97448-9c2b-4ea9-a237-4f82b2516c55'), editable=False, unique=True),
        ),
    ]
