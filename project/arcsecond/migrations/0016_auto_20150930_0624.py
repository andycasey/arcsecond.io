# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0015_auto_20150929_0720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='esoarchivedatarow',
            name='header_url',
        ),
        migrations.AddField(
            model_name='esoarchivedatarow',
            name='coordinates',
            field=models.ForeignKey(related_name='eso_archive_data_rows', blank=True, to='arcsecond.AstronomicalCoordinates', null=True),
        ),
        migrations.AddField(
            model_name='esoarchivedatarow',
            name='object_field',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
