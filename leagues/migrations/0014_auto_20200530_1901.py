# Generated by Django 2.2.12 on 2020-05-30 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0013_leaguesettings_auto_matchup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaguedivision',
            old_name='games',
            new_name='matches',
        ),
    ]
