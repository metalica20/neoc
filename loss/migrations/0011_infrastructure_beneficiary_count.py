# Generated by Django 2.1.5 on 2019-04-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loss', '0010_auto_20190412_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='infrastructure',
            name='beneficiary_count',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Beneficiary Count'),
        ),
    ]