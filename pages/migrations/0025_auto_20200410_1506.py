# Generated by Django 2.2.3 on 2020-04-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0024_auto_20200108_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticinfo',
            name='block1_img',
            field=models.ImageField(blank=True, upload_to='carousel_images'),
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='block1link',
            field=models.URLField(blank=True, default='https://www.google.com', null=True),
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='block1text',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='block2_img',
            field=models.ImageField(blank=True, upload_to='carousel_images'),
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='block2link',
            field=models.URLField(blank=True, default='https://www.google.com', null=True),
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='block2text',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='block3_img',
            field=models.ImageField(blank=True, upload_to='carousel_images'),
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='block3link',
            field=models.URLField(blank=True, default='https://www.google.com', null=True),
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='block3text',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='slide1header',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='slide1subhead',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='slide2header',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='slide2subhead',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='slide3header',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staticinfo',
            name='slide3subhead',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
