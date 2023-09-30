# Generated by Django 4.0.6 on 2023-02-14 15:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0048_resetpassword_status_alter_device_uniqid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('6f7359c7-b90c-4715-9b35-a43ee70174f5'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='resetpassword',
            name='resetUniqid',
            field=models.CharField(default=uuid.uuid4, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='resetpassword',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
