# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='use_2fa',
            field=models.BooleanField(default=False),
        ),
    ]
