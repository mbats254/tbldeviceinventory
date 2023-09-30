# Generated by Django 4.0.6 on 2023-02-24 10:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0034_alter_task_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('f9aa84de-8335-497f-9095-6d4a87e76f49'), editable=False, unique=True),
        ),
    ]
