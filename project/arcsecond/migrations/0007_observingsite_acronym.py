# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0006_auto_20150918_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='observingsite',
            name='acronym',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
        ),
    ]
