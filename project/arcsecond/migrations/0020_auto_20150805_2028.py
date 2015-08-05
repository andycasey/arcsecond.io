# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0019_auto_20150805_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coordinatesconversion',
            old_name='coords_CIRS',
            new_name='CIRS',
        ),
        migrations.AddField(
            model_name='coordinatesconversion',
            name='FK4',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.FK4Coordinates'),
        ),
        migrations.AddField(
            model_name='coordinatesconversion',
            name='FK4noETerms',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.FK4NoETermsCoordinates'),
        ),
        migrations.AddField(
            model_name='coordinatesconversion',
            name='FK5',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.FK5Coordinates'),
        ),
        migrations.AddField(
            model_name='coordinatesconversion',
            name='GCRS',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.GCRSCoordinates'),
        ),
        migrations.AddField(
            model_name='coordinatesconversion',
            name='Galactic',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.GalacticCoordinates'),
        ),
        migrations.AddField(
            model_name='coordinatesconversion',
            name='ICRS',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.ICRSCoordinates'),
        ),
    ]
