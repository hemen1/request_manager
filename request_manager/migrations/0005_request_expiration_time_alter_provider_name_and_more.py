# Generated by Django 4.2.5 on 2023-09-22 07:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_manager', '0004_request_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='expiration_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='execution_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 22, 7, 34, 0, 677999), null=True),
        ),
    ]
