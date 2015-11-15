# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0033_auto_20151115_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliation',
            name='organisation',
            field=models.ManyToManyField(related_name='affiliations', to='arcsecond.Organisation', blank=True),
        ),
    ]
