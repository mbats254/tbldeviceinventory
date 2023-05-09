# Generated by Django 4.0.6 on 2023-03-07 11:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0035_alter_task_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('bf52e0d1-ec70-44c5-847d-134fa0947984'), editable=False, unique=True),
        ),
    ]
