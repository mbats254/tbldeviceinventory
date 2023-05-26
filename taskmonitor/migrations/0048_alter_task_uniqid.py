# Generated by Django 4.2 on 2023-05-22 16:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('taskmonitor', '0047_alter_task_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uniqid',
            field=models.UUIDField(default=uuid.UUID('de020871-237b-4880-b60d-4e9eb0cdf54b'), editable=False, unique=True),
        ),
    ]
