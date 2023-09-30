# Generated by Django 4.0.6 on 2023-02-19 21:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0052_alter_device_uniqid_alter_devicetype_uniqid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('5d9dd6f0-f7ab-45aa-b576-78ab63052e22'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='devicetype',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('7a449083-e00b-46f0-9669-e35e1d270ad6'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('62af916c-29f6-4fc6-95bf-195213ddffc4'), editable=False, max_length=35, unique=True),
        ),
    ]
