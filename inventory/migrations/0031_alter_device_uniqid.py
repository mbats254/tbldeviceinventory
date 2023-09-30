# Generated by Django 4.0.6 on 2022-07-07 23:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0030_tokenstore_alter_device_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('f4a3fcdb-a3a4-486e-a6dd-fa3911d6a06c'), editable=False, max_length=35, unique=True),
        ),
    ]
