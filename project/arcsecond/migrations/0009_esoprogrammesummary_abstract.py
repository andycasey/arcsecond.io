# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0008_auto_20150725_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='esoprogrammesummary',
            name='abstract',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
    ]
