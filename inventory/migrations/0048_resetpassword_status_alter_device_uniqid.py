# Generated by Django 4.0.6 on 2023-02-12 16:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0047_resetpassword_alter_device_uniqid'),
    ]

    operations = [
        migrations.AddField(
            model_name='resetpassword',
            name='status',
            field=models.IntegerField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('df263df1-9007-44cb-8a0c-7f4e873f16d3'), editable=False, max_length=35, unique=True),
        ),
    ]
