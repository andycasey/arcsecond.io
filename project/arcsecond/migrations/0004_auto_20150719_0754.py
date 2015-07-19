# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0003_auto_20150719_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='angulardistance',
            name='unit',
            field=models.CharField(default=b'arcsec', max_length=6, choices=[(b'arcsec', b'arcsec'), (b'arcmin', b'arcmin')]),
        ),
        migrations.AlterField(
            model_name='ellipseaxis',
            name='unit',
            field=models.CharField(default=b'astronomical unit', max_length=18, choices=[(b'astronomical unit', b'astronomical unit'), (b'sun radius', b'sun radius')]),
        ),
        migrations.AlterField(
            model_name='mass',
            name='unit',
            field=models.CharField(default=b'sun', max_length=7, choices=[(b'sun', b'Sun'), (b'jupiter', b'Jupiter'), (b'neptune', b'Neptune'), (b'earth', b'Earth')]),
        ),
        migrations.AlterField(
            model_name='radius',
            name='unit',
            field=models.CharField(default=b'sun', max_length=7, choices=[(b'sun', b'Sun'), (b'jupiter', b'Jupiter'), (b'neptune', b'Neptune'), (b'earth', b'Earth')]),
        ),
    ]
