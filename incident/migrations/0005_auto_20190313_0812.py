# Generated by Django 2.1.5 on 2019-03-13 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0004_incident_reported_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='inducer',
            field=models.CharField(blank=True, choices=[('non_natural', 'Non Natural'), ('natural', 'Natural')], default=None, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='loss',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incident', to='loss.Loss'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='wards',
            field=models.ManyToManyField(blank=True, related_name='incidents', to='federal.Ward'),
        ),
    ]