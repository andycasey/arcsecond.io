# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0003_gcncircular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gcncircular',
            name='submitter',
            field=models.ForeignKey(related_name='submitted_GCN_circulars', blank=True, to='arcsecond.Person', null=True),
        ),
    ]
