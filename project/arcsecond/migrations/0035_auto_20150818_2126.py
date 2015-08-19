# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0034_auto_20150818_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='findingchart',
            name='height',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='findingchart',
            name='width',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
    ]
