# Generated by Django 2.1.5 on 2019-06-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_userprofile_email_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('user', 'Standard User'), ('admin', 'Admin'), ('superadmin', 'Super Admin')], default='user', max_length=10),
        ),
    ]
