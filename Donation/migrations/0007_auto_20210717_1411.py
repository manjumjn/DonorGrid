# Generated by Django 3.2.5 on 2021-07-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donation', '0006_donation_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='note',
            field=models.CharField(blank=True, default='', max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='on_behalf_of',
            field=models.CharField(blank=True, default='', max_length=256, null=True),
        ),
    ]