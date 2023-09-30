# Generated by Django 4.0.6 on 2023-06-14 13:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0069_returntooffice_alter_devicetype_uniqid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returntooffice',
            name='allocation_uniqid',
        ),
        migrations.AddField(
            model_name='member',
            name='phone_number',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='physical_address',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='techno_brain_email',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='devicetype',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('8db4649d-f66e-497f-86bf-4529c0cb928a'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('7f841b1b-d733-44b2-90b5-1e4b7c7662bd'), editable=False, max_length=35, unique=True),
        ),
    ]