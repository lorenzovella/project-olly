# Generated by Django 2.2.12 on 2020-05-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0012_auto_20200516_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaguesettings',
            name='auto_matchup',
            field=models.BooleanField(default=False),
        ),
    ]
