# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0017_auto_20150930_0644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='esoarchivedatarow',
            name='exposure_time',
        ),
    ]
