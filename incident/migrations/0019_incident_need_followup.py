# Generated by Django 2.1.5 on 2019-04-22 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0018_auto_20190422_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='need_followup',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]