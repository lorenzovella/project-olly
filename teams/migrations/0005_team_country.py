# Generated by Django 2.1.5 on 2019-02-08 17:40

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_merge_20181109_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]
