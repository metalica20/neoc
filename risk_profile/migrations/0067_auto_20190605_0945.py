# Generated by Django 2.1.5 on 2019-06-05 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_profile', '0066_auto_20190605_0843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='layertable',
            old_name='sub_category',
            new_name='filter_options',
        ),
        migrations.RenameField(
            model_name='layertable',
            old_name='layer_name',
            new_name='layername',
        ),
        migrations.RenameField(
            model_name='layertable',
            old_name='layer_tbl',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='layertable',
            name='layer_cat',
        ),
        migrations.RemoveField(
            model_name='layertable',
            name='upload_type',
        ),
    ]
