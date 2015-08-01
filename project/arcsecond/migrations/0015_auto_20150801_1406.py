# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0014_auto_20150801_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alias',
            name='catalogue_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='astronomicalcoordinates',
            name='declination',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='astronomicalcoordinates',
            name='right_ascension',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
