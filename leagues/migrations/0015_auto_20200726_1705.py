# Generated by Django 2.2.14 on 2020-07-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0014_auto_20200530_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='prize1',
            field=models.CharField(default='no prize specified', max_length=50),
        ),
        migrations.AddField(
            model_name='league',
            name='prize2',
            field=models.CharField(default='no prize specified', max_length=50),
        ),
        migrations.AddField(
            model_name='league',
            name='prize3',
            field=models.CharField(default='no prize specified', max_length=50),
        ),
    ]
