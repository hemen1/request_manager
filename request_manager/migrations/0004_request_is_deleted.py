# Generated by Django 4.2.5 on 2023-09-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_manager', '0003_alter_request_executed_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
