# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0016_auto_20150801_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoordinatesConversion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input_coordinates', models.OneToOneField(null=True, blank=True, to='arcsecond.AstronomicalCoordinates')),
            ],
        ),
    ]
