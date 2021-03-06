# Generated by Django 2.2.7 on 2020-01-15 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0018_match_disable_userreports'),
        ('singletournaments', '0017_singleeliminationtournament_disable_userreports'),
    ]

    operations = [
        migrations.AddField(
            model_name='singleeliminationtournament',
            name='sports',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sport', to='matches.SportChoice'),
        ),
        migrations.AlterField(
            model_name='singleeliminationtournament',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='game', to='matches.GameChoice'),
        ),
        migrations.AlterField(
            model_name='singleeliminationtournament',
            name='platform',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='matches.PlatformChoice'),
        ),
    ]
