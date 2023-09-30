# Generated by Django 4.0.6 on 2023-02-14 21:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0027_alter_task_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('2f20b52d-caf8-49bd-a559-c65cb4677098'), editable=False, unique=True),
        ),
    ]
