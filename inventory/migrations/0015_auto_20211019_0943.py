# Generated by Django 3.2.8 on 2021-10-19 09:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20211019_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('171a5bb5-6b9f-4cf7-9dcf-d9ee910a1fce'), max_length=70),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('104b3650-fa06-41ba-adbd-1b6e9b70fdcf'), max_length=70),
        ),
        migrations.AlterField(
            model_name='damageddevice',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('83fcc9f3-5199-4525-8da0-366e8b6acfa9'), max_length=70),
        ),
        migrations.AlterField(
            model_name='device',
            name='serial_number',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('9c4960fb-8c1d-4d29-a63f-71f8dbc76255'), max_length=70),
        ),
        migrations.AlterField(
            model_name='member',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('f05b3f61-6ef3-49f2-b035-c3586687bfa0'), max_length=70),
        ),
        migrations.AlterField(
            model_name='team',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('0fd30c57-a302-45c3-a5b7-0b0835a30889'), max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='teamallocation',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('b62490aa-8615-4bad-9926-bde56098f5b8'), max_length=70),
        ),
        migrations.AlterField(
            model_name='teamlead',
            name='user_uniqid',
            field=models.CharField(default=uuid.UUID('3a33fb93-82d4-461a-85ca-ac0b993fb277'), max_length=70),
        ),
    ]
