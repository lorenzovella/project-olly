# Generated by Django 2.0.1 on 2018-06-29 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20180623_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='current_earning',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
