# Generated by Django 4.0.6 on 2022-07-06 09:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0004_remove_task_taskid_remove_task_task_card_uniqid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('bd4f507e-c2fb-454b-b69b-8f57ec730ea7'), editable=False, unique=True),
        ),
    ]
