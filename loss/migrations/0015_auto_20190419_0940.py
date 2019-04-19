# Generated by Django 2.1.5 on 2019-04-19 09:40

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('loss', '0014_auto_20190419_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agriculturetype',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='loss.AgricultureType'),
        ),
    ]
