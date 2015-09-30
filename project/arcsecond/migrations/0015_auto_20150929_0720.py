# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0014_fitsheaderrow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esoarchivedatarow',
            name='summary',
            field=models.ForeignKey(related_name='data_rows', blank=True, to='arcsecond.ESOProgrammeSummary', null=True),
        ),
    ]
