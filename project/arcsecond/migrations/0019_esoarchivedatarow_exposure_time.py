# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0018_remove_esoarchivedatarow_exposure_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='esoarchivedatarow',
            name='exposure_time',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=6, blank=True),
        ),
    ]
