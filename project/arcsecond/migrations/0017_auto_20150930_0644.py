# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0016_auto_20150930_0624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='esoarchivedatarow',
            name='modified_julian_date',
        ),
        migrations.AlterField(
            model_name='esoarchivedatarow',
            name='exposure_time',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
