# Generated by Django 4.0.6 on 2022-07-24 13:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0033_alter_device_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocation',
            name='user_team',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('6cc7db87-e2b7-4ace-bb8d-0f014f60ab6c'), editable=False, max_length=35, unique=True),
        ),
    ]
