# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0013_auto_20150801_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exoplanet',
            old_name='velocity_semiamplitude_K',
            new_name='velocity_semiamplitude',
        ),
        migrations.RemoveField(
            model_name='exoplanet',
            name='impact_parameter_b',
        ),
        migrations.RemoveField(
            model_name='exoplanet',
            name='omega',
        ),
        migrations.RemoveField(
            model_name='exoplanet',
            name='time_vr0',
        ),
        migrations.AddField(
            model_name='astronomicalobject',
            name='age',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.Age'),
        ),
        migrations.AddField(
            model_name='astronomicalobject',
            name='distance',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.Distance'),
        ),
        migrations.AddField(
            model_name='astronomicalobject',
            name='effective_temperature',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.Temperature'),
        ),
        migrations.AddField(
            model_name='astronomicalobject',
            name='metallicity',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.Metallicity'),
        ),
        migrations.AddField(
            model_name='astronomicalobject',
            name='radius',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.Radius'),
        ),
        migrations.AddField(
            model_name='astronomicalobject',
            name='spectral_type',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='impact_parameter',
            field=models.OneToOneField(related_name='impact_parameter', null=True, blank=True, to='arcsecond.Angle'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='lambda_angle',
            field=models.OneToOneField(related_name='lambda_angle', null=True, blank=True, to='arcsecond.Angle'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='omega_angle',
            field=models.OneToOneField(related_name='omega_angle', null=True, blank=True, to='arcsecond.Angle'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='publication_status',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='time_conjonction',
            field=models.OneToOneField(related_name='time_conjonction', null=True, blank=True, to='arcsecond.JulianDay'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='time_radial_velocity_zero',
            field=models.OneToOneField(related_name='time_radial_velocity_zero', null=True, blank=True, to='arcsecond.JulianDay'),
        ),
        migrations.AlterField(
            model_name='exoplanet',
            name='molecules_detected',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='exoplanet',
            name='orbital_period',
            field=models.OneToOneField(related_name='orbital_period', null=True, blank=True, to='arcsecond.Period'),
        ),
        migrations.AlterField(
            model_name='exoplanet',
            name='semi_major_axis',
            field=models.OneToOneField(related_name='semi_major_axis', null=True, blank=True, to='arcsecond.EllipseAxis'),
        ),
        migrations.AlterField(
            model_name='mass',
            name='unit',
            field=models.CharField(default=b'sun', max_length=3, choices=[(b'sun', b'Msun'), (b'jup', b'Mjup'), (b'nep', b'Mnep'), (b'ear', b'Mearth')]),
        ),
        migrations.AlterField(
            model_name='radius',
            name='unit',
            field=models.CharField(default=b'sun', max_length=3, choices=[(b'sun', b'Rsun'), (b'jup', b'Rjup'), (b'nep', b'Rnep'), (b'ear', b'Rearth')]),
        ),
    ]
