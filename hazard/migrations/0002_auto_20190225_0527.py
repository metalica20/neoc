# Generated by Django 2.1.5 on 2019-02-25 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hazard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hazard',
            name='icon',
            field=models.CharField(blank=True, default=None, max_length=25, null=True),
        ),
    ]