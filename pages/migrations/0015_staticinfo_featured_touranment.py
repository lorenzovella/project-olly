# Generated by Django 2.1.5 on 2019-03-13 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('singletournaments', '0012_auto_20190112_1546'),
        ('pages', '0014_remove_staticinfo_featured_touranment'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticinfo',
            name='featured_touranment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='featured_tournamet', to='singletournaments.SingleEliminationTournament'),
        ),
    ]
