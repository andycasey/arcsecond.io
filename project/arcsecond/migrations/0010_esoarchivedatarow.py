# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0009_auto_20150921_0604'),
    ]

    operations = [
        migrations.CreateModel(
            name='ESOArchiveDataRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header_url', models.URLField()),
                ('more_url', models.URLField()),
                ('seeing_url', models.URLField()),
                ('instrument_name', models.CharField(max_length=100, null=True, blank=True)),
                ('dataset_id', models.CharField(max_length=100, null=True, blank=True)),
                ('exposure_time', models.FloatField(null=True, blank=True)),
                ('modified_julian_date', models.FloatField(null=True, blank=True)),
                ('summary', models.OneToOneField(null=True, blank=True, to='arcsecond.ESOProgrammeSummary')),
                ('telescope', models.ForeignKey(related_name='data_row', blank=True, to='arcsecond.Telescope', null=True)),
            ],
        ),
    ]
