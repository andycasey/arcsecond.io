# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields.ranges


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0031_auto_20151109_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='affiliation',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='affiliation',
            name='start_date',
        ),
        migrations.AddField(
            model_name='affiliation',
            name='dates',
            field=django.contrib.postgres.fields.ranges.DateRangeField(null=True, blank=True),
        ),
    ]
