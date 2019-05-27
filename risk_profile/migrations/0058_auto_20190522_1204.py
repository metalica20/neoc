# Generated by Django 2.1.5 on 2019-05-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0057_auto_20190522_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Culturalv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'cultural_views',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Educationv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'education_views',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Financev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'finance_views',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Governancev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'governance_views',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='hazardlayer',
            name='about',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='hazardsublayerdetail',
            name='center',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hazardsublayerdetail',
            name='layername',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hazardtype',
            name='about',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
