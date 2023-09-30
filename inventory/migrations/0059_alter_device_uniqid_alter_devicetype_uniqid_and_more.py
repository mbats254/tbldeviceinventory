# Generated by Django 4.0.6 on 2023-03-07 11:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0058_alter_device_uniqid_alter_devicetype_uniqid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('3c4f4b9c-fa99-45bd-a675-153486d98f3b'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='devicetype',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('8bf3d4b7-62c0-441e-811b-bbd28888920a'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('a4a14cd4-e21a-45aa-a816-80edfd522ee9'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='uniqid',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=35, unique=True),
        ),
    ]
