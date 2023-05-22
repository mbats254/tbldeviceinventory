# Generated by Django 4.0.6 on 2023-05-22 10:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0068_alter_devicetype_uniqid_alter_notification_uniqid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnToOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_uniqid', models.CharField(max_length=70)),
                ('allocation_uniqid', models.CharField(blank=True, max_length=70, null=True)),
                ('condition', models.CharField(max_length=70)),
                ('user_uniqid', models.CharField(max_length=70)),
                ('uniqid', models.CharField(default=uuid.uuid4, editable=False, max_length=35, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='devicetype',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('f35be347-9607-4cbe-83d0-3409b676968a'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('d41196b3-495d-427c-b772-3b2593b4f6a4'), editable=False, max_length=35, unique=True),
        ),
    ]