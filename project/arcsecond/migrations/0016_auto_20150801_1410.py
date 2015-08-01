# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0015_auto_20150801_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exoplanet',
            name='discovery_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='exoplanet',
            name='last_update',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
