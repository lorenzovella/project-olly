# Generated by Django 2.0.5 on 2018-07-03 23:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('website', models.URLField(blank=True, default='#')),
                ('twitter', models.CharField(blank=True, default='#', max_length=100)),
                ('bio', models.TextField()),
                ('logo', models.ImageField(blank=True, upload_to='partner_images')),
            ],
        ),
        migrations.CreateModel(
            name='StaticInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.TextField(default='about us')),
                ('terms', models.TextField(default='terms of service')),
                ('privacy', models.TextField(default='privacy policy')),
                ('stream', models.CharField(default='twitch', max_length=25)),
                ('slide1link', models.TextField(default='#')),
                ('slide2link', models.TextField(default='#')),
                ('slide3link', models.TextField(default='#')),
            ],
        ),
    ]
