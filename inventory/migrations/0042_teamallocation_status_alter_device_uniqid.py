# Generated by Django 4.0.6 on 2023-01-17 10:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0041_member_user_photo_alter_device_uniqid'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamallocation',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('85e0be3b-4cb4-4810-89c4-7c3829b205d5'), editable=False, max_length=35, unique=True),
        ),
    ]
