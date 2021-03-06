# Generated by Django 2.1.7 on 2019-03-16 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_auto_20190112_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default_map', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('map_num', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_for', to='matches.GameChoice')),
            ],
        ),
        migrations.CreateModel(
            name='MapPoolChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default map pool', max_length=255)),
                ('description', models.CharField(default='No map pool description', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_pool_for', to='matches.GameChoice')),
                ('maps', models.ManyToManyField(to='matches.MapChoice')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='map',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='match_map', to='matches.MapChoice'),
        ),
    ]
