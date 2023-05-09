# Generated by Django 4.0.6 on 2023-02-19 12:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0028_alter_task_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('d9662599-fcd4-4f37-a964-574b5837135b'), editable=False, unique=True),
        ),
    ]
