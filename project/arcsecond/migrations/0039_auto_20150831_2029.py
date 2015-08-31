# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0038_auto_20150831_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='coordinates',
            field=models.ManyToManyField(related_name='building', null=True, to='arcsecond.Coordinates', blank=True),
        ),
        migrations.AlterField(
            model_name='telescope',
            name='dome',
            field=models.OneToOneField(related_name='telescope', null=True, blank=True, to='arcsecond.Dome'),
        ),
    ]
