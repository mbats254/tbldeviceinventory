# Generated by Django 3.2.8 on 2021-10-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DamagedDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_uniqid', models.CharField(max_length=70)),
                ('team_allocated', models.CharField(max_length=70)),
                ('explained_issue', models.CharField(max_length=300)),
                ('uniqid', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TeamAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_uniqid', models.CharField(max_length=70)),
                ('team_allocated', models.CharField(max_length=70)),
                ('uniqid', models.CharField(max_length=70)),
            ],
        ),
        migrations.AddField(
            model_name='allocation',
            name='location',
            field=models.CharField(default='home', max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='allocation',
            name='use',
            field=models.CharField(default='test bed', max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='RAM',
            field=models.CharField(blank=True, default=None, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='capacity',
            field=models.CharField(blank=True, default=None, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='processor',
            field=models.CharField(blank=True, default=None, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='storage_type',
            field=models.CharField(blank=True, default=None, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='type',
            field=models.CharField(default='desktop', max_length=70),
            preserve_default=False,
        ),
    ]
