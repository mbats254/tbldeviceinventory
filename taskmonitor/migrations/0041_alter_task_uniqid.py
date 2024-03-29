# Generated by Django 4.0.6 on 2023-05-05 09:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0040_alter_task_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('b1397bdd-4ef7-4c16-a565-b0d0e89048b2'), editable=False, unique=True),
        ),
    ]
