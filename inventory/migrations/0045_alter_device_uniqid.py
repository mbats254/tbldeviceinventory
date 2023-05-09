# Generated by Django 4.0.6 on 2023-02-12 15:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0044_alter_device_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('34b5ba9e-a9cb-416a-b36c-2b0aa4e1ac09'), editable=False, max_length=35, unique=True),
        ),
    ]
