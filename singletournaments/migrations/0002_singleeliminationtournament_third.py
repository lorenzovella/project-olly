# Generated by Django 2.0.7 on 2018-07-08 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('teams', '0001_initial'),
        ('singletournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='singleeliminationtournament',
            name='third',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='thirdplaceteam', to='teams.Team'),
        ),
    ]
