# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0018_cirscoordinates_fk4coordinates_fk4noetermscoordinates_fk5coordinates_galacticcoordinates_gcrscoordin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coordinatesconversion',
            name='input_coordinates',
        ),
        migrations.AddField(
            model_name='coordinatesconversion',
            name='coords_CIRS',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.CIRSCoordinates'),
        ),
        migrations.AddField(
            model_name='coordinatesconversion',
            name='input_first_value',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='coordinatesconversion',
            name='input_frame',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='coordinatesconversion',
            name='input_second_value',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
