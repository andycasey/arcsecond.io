# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0030_timesconversion'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesconversion',
            name='input_format',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
