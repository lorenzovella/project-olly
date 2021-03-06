# Generated by Django 2.0.5 on 2018-07-03 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BannedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(default='error', max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banned',
                                           to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserGear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownpc', models.BooleanField(default=False)),
                ('cpu', models.CharField(default='No CPU specified', max_length=30)),
                ('gpu', models.CharField(default='No GPU specified', max_length=30)),
                ('psu', models.CharField(default='No PSU specified', max_length=30)),
                ('case', models.CharField(default='No Case specified', max_length=30)),
                ('os', models.CharField(default='No OS specified', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userspecs',
                                           to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xp', models.PositiveSmallIntegerField(default=0)),
                ('credits', models.PositiveSmallIntegerField(default=0)),
                ('passes', models.PositiveSmallIntegerField(default=0)),
                ('total_earning', models.PositiveSmallIntegerField(default=0)),
                ('current_earning', models.PositiveSmallIntegerField(default=0)),
                ('about_me', models.TextField(blank=True, default='Forever a mystery')),
                ('xbl', models.CharField(blank=True, default='No Xbox Live Linked', max_length=30)),
                ('psn', models.CharField(blank=True, default='No PSN Linked', max_length=30)),
                ('steam', models.CharField(blank=True, default='No Steam Linked', max_length=30)),
                ('lol', models.CharField(blank=True, default='No LOL Linked', max_length=30)),
                ('battlenet', models.CharField(blank=True, default='No Battle.net Linked', max_length=30)),
                ('twitter_profile', models.CharField(blank=True, default='No Twitter Linked', max_length=30)),
                ('twitch_channel', models.CharField(blank=True, default='No Twitch Linked', max_length=50)),
                ('favorite_game', models.CharField(blank=True, default='N/A', max_length=50)),
                ('favorite_console', models.CharField(blank=True, default='N/A', max_length=50)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user_type', models.CharField(default='user', max_length=10)),
                ('ip', models.CharField(default='0.0.0.0', max_length=16)),
                ('num_trophies', models.PositiveSmallIntegerField(default=0)),
                ('xbl_verified', models.BooleanField(default=False)),
                ('psn_verified', models.BooleanField(default=False)),
                ('num_bronze', models.PositiveSmallIntegerField(default=0)),
                ('num_silver', models.PositiveSmallIntegerField(default=0)),
                ('num_gold', models.PositiveSmallIntegerField(default=0)),
                ('num_plat', models.PositiveSmallIntegerField(default=0)),
                ('num_diamond', models.PositiveSmallIntegerField(default=0)),
                ('num_titanium', models.PositiveSmallIntegerField(default=0)),
                ('tournament_wins', models.PositiveSmallIntegerField(default=0)),
                ('dubl_tournament_wins', models.PositiveSmallIntegerField(default=0)),
                ('country', django_countries.fields.CountryField(default='US', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user',
                                              to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
