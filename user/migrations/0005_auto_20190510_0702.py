# Generated by Django 2.1.5 on 2019-05-10 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190506_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, default=None, max_length=17, null=True),
        ),
    ]