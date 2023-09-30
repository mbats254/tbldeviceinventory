# Generated by Django 4.0.6 on 2022-07-07 23:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0008_alter_task_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('669a264d-50fc-4bba-b88d-af29febbc684'), editable=False, unique=True),
        ),
    ]
