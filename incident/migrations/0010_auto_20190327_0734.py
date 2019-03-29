# Generated by Django 2.1.5 on 2019-03-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0009_incident_old'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incident',
            options={'permissions': [('can_verify', 'Can verify incident'),
                                     ('can_approve', 'Can approve incident')]},
        ),
        migrations.AddField(
            model_name='incident',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]