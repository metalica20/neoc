# Generated by Django 2.1.5 on 2019-02-17 02:32

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('federal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, default=None, null=True, srid=4326)),
                ('detail', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resources.Resource')),
                ('no_of_classrooms', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('resources.resource',),
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resources.Resource')),
                ('no_of_beds', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('resources.resource',),
        ),
        migrations.AddField(
            model_name='resource',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_resources.resource_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='resource',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resources', to='federal.Ward'),
        ),
    ]