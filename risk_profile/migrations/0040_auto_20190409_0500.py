# Generated by Django 2.1.5 on 2019-04-09 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0039_testw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testw',
            name='name',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
