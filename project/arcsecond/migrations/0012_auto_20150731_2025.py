# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0011_auto_20150728_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exoplanet',
            name='angular_distance',
            field=models.OneToOneField(related_name='angular_distance', null=True, blank=True, to='arcsecond.AngularDistance'),
        ),
    ]
