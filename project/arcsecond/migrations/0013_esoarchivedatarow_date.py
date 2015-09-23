# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0012_auto_20150923_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='esoarchivedatarow',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True),
        ),
    ]
