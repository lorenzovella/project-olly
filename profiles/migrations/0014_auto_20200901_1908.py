# Generated by Django 2.2.15 on 2020-09-01 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_notification_pk1'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='discord',
            field=models.CharField(blank=True, default='No Dsicord', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='steamid64',
            field=models.CharField(blank=True, default='No SteamID64', max_length=255),
        ),
    ]
