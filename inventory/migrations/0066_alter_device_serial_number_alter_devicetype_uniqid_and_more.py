# Generated by Django 4.0.6 on 2023-05-09 12:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0065_alter_devicetype_uniqid_alter_notification_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='serial_number',
            field=models.CharField(max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='devicetype',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('daab658c-2aab-42dc-8dc5-b6375b836446'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('46eade6f-04bd-40ad-834e-b9e953c85604'), editable=False, max_length=35, unique=True),
        ),
    ]
