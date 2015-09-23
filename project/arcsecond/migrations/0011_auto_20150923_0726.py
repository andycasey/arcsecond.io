# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0010_esoarchivedatarow'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataArchive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('organisations', models.ManyToManyField(related_name='archive', null=True, to='arcsecond.AstronomicalOrganisation', blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='esoarchivedatarow',
            name='dataset_id',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='esoarchivedatarow',
            name='telescope',
            field=models.ForeignKey(related_name='data_rows', blank=True, to='arcsecond.Telescope', null=True),
        ),
        migrations.AddField(
            model_name='esoarchivedatarow',
            name='archive',
            field=models.ForeignKey(related_name='data_rows', blank=True, to='arcsecond.DataArchive', null=True),
        ),
    ]
