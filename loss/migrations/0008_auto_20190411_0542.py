# Generated by Django 2.1.5 on 2019-04-11 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loss', '0007_auto_20190404_0724'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='family',
            options={'verbose_name': 'Family', 'verbose_name_plural': 'families'},
        ),
        migrations.AlterModelOptions(
            name='infrastructure',
            options={'verbose_name': 'Infrastructure', 'verbose_name_plural': 'infrastructures'},
        ),
        migrations.AlterModelOptions(
            name='livestock',
            options={'verbose_name': 'Livestock', 'verbose_name_plural': 'livestocks'},
        ),
        migrations.AlterModelOptions(
            name='loss',
            options={'verbose_name': 'Loss', 'verbose_name_plural': 'losses'},
        ),
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name': 'People', 'verbose_name_plural': 'People'},
        ),
        migrations.AlterField(
            model_name='family',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='family',
            name='below_poverty',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Below Poverty'),
        ),
        migrations.AlterField(
            model_name='family',
            name='count',
            field=models.PositiveIntegerField(default=1, verbose_name='Count'),
        ),
        migrations.AlterField(
            model_name='family',
            name='phone_number',
            field=models.CharField(blank=True, default=None, max_length=25, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='family',
            name='status',
            field=models.CharField(choices=[('affected', 'Affected'), ('relocated', 'Relocated'), ('evacuated', 'Evacuated')], max_length=25, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='family',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='beneficiary_owner',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Beneficiary Owner'),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='count',
            field=models.PositiveIntegerField(default=1, verbose_name='Count'),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='economic_loss',
            field=models.BigIntegerField(blank=True, default=None, null=True, verbose_name='Economic Loss'),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='equipment_value',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Equipment Value'),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='infrastructure_value',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Infrastructure Value'),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='resource',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='resources.Resource', verbose_name='Resource'),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='service_disrupted',
            field=models.BooleanField(blank=True, default=None, max_length=255, null=True, verbose_name='Service Disrupted'),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='status',
            field=models.CharField(choices=[('destroyed', 'Destroyed'), ('affected', 'Affected')], max_length=25, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='infrastructures', to='loss.InfrastructureType', verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='livestock',
            name='count',
            field=models.PositiveIntegerField(verbose_name='Count'),
        ),
        migrations.AlterField(
            model_name='livestock',
            name='economic_loss',
            field=models.BigIntegerField(blank=True, default=None, null=True, verbose_name='Economic Loss'),
        ),
        migrations.AlterField(
            model_name='livestock',
            name='status',
            field=models.CharField(choices=[('destroyed', 'Destroyed'), ('affected', 'Affected')], max_length=25, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='livestock',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='livestock',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='livestocks', to='loss.LivestockType', verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='loss',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='loss',
            name='estimated_loss',
            field=models.BigIntegerField(blank=True, default=None, null=True, verbose_name='Estimated Loss'),
        ),
        migrations.AlterField(
            model_name='people',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='people',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='people',
            name='below_poverty',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Below Poverty'),
        ),
        migrations.AlterField(
            model_name='people',
            name='count',
            field=models.PositiveIntegerField(default=1, verbose_name='Count'),
        ),
        migrations.AlterField(
            model_name='people',
            name='disabled',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Disabled'),
        ),
        migrations.AlterField(
            model_name='people',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], default=None, max_length=25, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='people',
            name='status',
            field=models.CharField(choices=[('dead', 'Dead'), ('missing', 'Missing'), ('injured', 'Injured'), ('affected', 'Affected')], max_length=25, verbose_name='Status'),
        ),
    ]
