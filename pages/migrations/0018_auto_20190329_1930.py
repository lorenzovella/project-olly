# Generated by Django 2.1.5 on 2019-03-29 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20190328_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticinfo',
            name='featured_tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='featured_tournament', to='singletournaments.SingleEliminationTournament'),
        ),
    ]
