# Generated by Django 2.0.1 on 2018-03-29 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20180329_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='twitter_profile',
            field=models.CharField(blank=True, default='No Twitter Linked', max_length=20),
        ),
    ]