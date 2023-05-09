# Generated by Django 3.2.8 on 2021-10-18 21:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20211017_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocation',
            name='user_team',
            field=models.CharField(default='qwqweqeeweqwe', max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admin',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('5053b20f-25e7-4462-a070-615da9da94c5'), max_length=70),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('59088c13-fed9-4d98-8c66-652bcff71d14'), max_length=70),
        ),
        migrations.AlterField(
            model_name='damageddevice',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('0f6e9f3b-6aa5-4565-9cc0-18165f7ad9d9'), max_length=70),
        ),
        migrations.AlterField(
            model_name='device',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('1d2b5c66-6285-4cde-9729-7e919fcbbc72'), max_length=70),
        ),
        migrations.AlterField(
            model_name='member',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('bce4a00d-2919-4ec3-9c1c-dda71c2328bb'), max_length=70),
        ),
        migrations.AlterField(
            model_name='team',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('0150b706-e217-49aa-92c0-e7e3506f331d'), max_length=70),
        ),
        migrations.AlterField(
            model_name='teamallocation',
            name='uniqid',
            field=models.CharField(default=uuid.UUID('b6e0a667-247e-4b04-921e-18425736664d'), max_length=70),
        ),
        migrations.AlterField(
            model_name='teamlead',
            name='user_uniqid',
            field=models.CharField(default=uuid.UUID('1fc57714-f197-4a43-990c-98a9a5f3efef'), max_length=70),
        ),
    ]
