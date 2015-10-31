# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0024_auto_20151030_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='membership_date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True),
        ),
    ]
