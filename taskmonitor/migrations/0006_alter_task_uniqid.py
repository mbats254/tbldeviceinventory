# Generated by Django 4.0.6 on 2022-07-06 09:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0005_alter_task_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('10ffbd6c-dacf-401f-948b-2aae267fffa5'), editable=False, unique=True),
        ),
    ]
