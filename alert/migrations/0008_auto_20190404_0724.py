# Generated by Django 2.1.5 on 2019-04-04 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0007_alert_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='source',
            field=models.CharField(choices=[('dhm', 'DHM'), ('other', 'Other'), ('nsc', 'NSC')], default='other', max_length=255),
        ),
    ]