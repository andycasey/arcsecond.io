# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0011_auto_20150923_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataarchive',
            name='organisations',
            field=models.ManyToManyField(related_name='archive', to='arcsecond.AstronomicalOrganisation', blank=True),
        ),
    ]
