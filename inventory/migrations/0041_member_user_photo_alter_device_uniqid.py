# Generated by Django 4.0.6 on 2022-10-16 12:11

from django.db import migrations, models
import inventory.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0040_alter_device_uniqid'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='user_photo',
            field=models.ImageField(blank=True, null=True, upload_to=inventory.models.upload_to),
        ),
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('5373a77d-d9d1-49da-8859-0a093bcb2349'), editable=False, max_length=35, unique=True),
        ),
    ]
