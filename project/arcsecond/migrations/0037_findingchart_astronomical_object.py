# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0036_auto_20150819_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='findingchart',
            name='astronomical_object',
            field=models.ForeignKey(related_name='finding_charts', blank=True, to='arcsecond.AstronomicalObject', null=True),
        ),
    ]
