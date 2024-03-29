# Generated by Django 4.0.6 on 2023-02-19 17:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0051_devicetype_rename_brand_device_devicetypeuniqid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('17edf1ff-bc15-48a3-9d23-49b6c7911b01'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='devicetype',
            name='uniqid',
            field=models.CharField(editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('b2bd0f1d-fd28-4cd8-86f0-bb56a2859a73'), editable=False, max_length=35, unique=True),
        ),
    ]
