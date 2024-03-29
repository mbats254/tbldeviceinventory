# Generated by Django 4.0.6 on 2023-05-05 09:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0062_alter_devicetype_poster_link_alter_devicetype_uniqid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicetype',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('1eb15d04-f9df-4f05-933b-e3334d5648a8'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('135cb10b-021a-4d7b-a969-29934ca4f9d7'), editable=False, max_length=35, unique=True),
        ),
    ]
