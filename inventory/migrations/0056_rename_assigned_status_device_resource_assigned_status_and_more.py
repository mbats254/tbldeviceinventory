# Generated by Django 4.0.6 on 2023-02-24 09:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0055_device_assigned_status_alter_device_uniqid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='assigned_status',
            new_name='resource_assigned_status',
        ),
        migrations.AddField(
            model_name='device',
            name='team_assigned_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('100f811d-d529-4ea9-853f-6edad55374de'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='devicetype',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('c9ac5e21-3431-4c56-a95b-6d2fa4f242a5'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('39ca21a0-e06b-4db7-a78c-817d2f4950d6'), editable=False, max_length=35, unique=True),
        ),
    ]
