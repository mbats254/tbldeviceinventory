# Generated by Django 4.0.2 on 2022-06-03 18:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0023_alter_device_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('f85e3646-2f76-48b9-aaaf-afb092687836'), editable=False, max_length=35, unique=True),
        ),
    ]
