# Generated by Django 3.2.5 on 2021-07-09 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Package', '0006_auto_20210708_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='gateway_keys',
            field=models.JSONField(default={}),
        ),
    ]