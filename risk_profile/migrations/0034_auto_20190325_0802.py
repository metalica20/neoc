# Generated by Django 2.1.5 on 2019-03-25 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0033_auto_20190325_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='atm_available',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=50, null=True),
        ),
    ]
