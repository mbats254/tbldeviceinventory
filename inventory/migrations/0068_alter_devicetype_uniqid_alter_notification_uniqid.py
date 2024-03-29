# Generated by Django 4.0.6 on 2023-05-09 13:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0067_alter_devicetype_uniqid_alter_member_team_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicetype',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('6cc9a2dc-c9c3-482c-b4a8-f719eb58ab50'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('2c026998-b55a-4e19-b90f-bf0d183adcfc'), editable=False, max_length=35, unique=True),
        ),
    ]
