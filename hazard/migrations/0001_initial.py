# Generated by Django 2.1.5 on 2019-02-17 02:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hazard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('icon', models.FileField(blank=True, default=None, null=True, upload_to='hazard-icons/')),
                ('style', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HazardResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(default=0)),
                ('hazard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hazard.Hazard')),
                ('resource', models.ForeignKey(limit_choices_to=models.Q(('app_label', 'resources'), models.Q(_negated=True, model='resource')), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.AddField(
            model_name='hazard',
            name='resources',
            field=models.ManyToManyField(through='hazard.HazardResources', to='contenttypes.ContentType'),
        ),
    ]
