# Generated by Django 4.0.6 on 2023-02-19 12:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0050_notification_alter_device_uniqid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('type', models.CharField(max_length=70)),
                ('brand', models.CharField(max_length=70)),
                ('poster', models.ImageField(null=True, upload_to='', verbose_name='images/')),
                ('capacity', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('storage_type', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('RAM', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('processor', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('uniqid', models.CharField(default=uuid.UUID('87771d2a-d686-4c68-8211-bf48bb6a65b3'), editable=False, max_length=35, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='device',
            old_name='brand',
            new_name='deviceTypeUniqid',
        ),
        migrations.RemoveField(
            model_name='device',
            name='RAM',
        ),
        migrations.RemoveField(
            model_name='device',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='device',
            name='name',
        ),
        migrations.RemoveField(
            model_name='device',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='device',
            name='processor',
        ),
        migrations.RemoveField(
            model_name='device',
            name='storage_type',
        ),
        migrations.RemoveField(
            model_name='device',
            name='type',
        ),
        migrations.AddField(
            model_name='notification',
            name='user_uniqid',
            field=models.CharField(default='sd', max_length=35),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('987405cc-e7ca-4d3f-a92e-baf817a9b942'), editable=False, max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('32e84806-7306-4079-bdeb-327c4d4828b8'), editable=False, max_length=35, unique=True),
        ),
    ]
