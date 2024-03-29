# Generated by Django 4.0.6 on 2022-07-06 09:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0028_rename_fullname_member_full_name_alter_device_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('b3ab8bb8-e981-4276-8963-cde43c63f8d2'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='full_name',
            field=models.CharField(default='tester', max_length=70),
        ),
    ]
