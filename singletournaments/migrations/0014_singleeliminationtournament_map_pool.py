# Generated by Django 2.1.7 on 2019-03-16 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0008_auto_20190315_2152'),
        ('singletournaments', '0013_auto_20190313_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='singleeliminationtournament',
            name='map_pool',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='map_pool', to='matches.MapPoolChoice'),
        ),
    ]
