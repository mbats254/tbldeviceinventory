# Generated by Django 3.2.8 on 2021-10-19 09:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_auto_20211019_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='uniqid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
