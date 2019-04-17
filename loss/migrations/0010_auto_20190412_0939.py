# Generated by Django 2.1.5 on 2019-04-12 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loss', '0009_auto_20190411_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='infrastructuretype',
            name='title_en',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='infrastructuretype',
            name='title_ne',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='livestocktype',
            name='title_en',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='livestocktype',
            name='title_ne',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
