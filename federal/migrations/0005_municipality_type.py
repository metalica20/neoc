# Generated by Django 2.1.5 on 2019-03-11 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('federal', '0004_auto_20190226_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipality',
            name='type',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]