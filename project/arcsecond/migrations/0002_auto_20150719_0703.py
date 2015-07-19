# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exoplanet',
            old_name='semimajor_axis',
            new_name='semi_major_axis',
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='angular_distance',
            field=models.OneToOneField(related_name='angular_distance', null=True, blank=True, to='arcsecond.Angle'),
        ),
        migrations.AlterField(
            model_name='exoplanet',
            name='detection_method',
            field=models.CharField(default=b'unk', max_length=3, blank=True, choices=[(b'unk', b'Unknown'), (b'rvs', b'Radial Velocity'), (b'mls', b'Microlensing'), (b'tra', b'Primary Transit'), (b'tim', b'Timing'), (b'ast', b'Astrometry'), (b'img', b'Imaging')]),
        ),
        migrations.AlterField(
            model_name='exoplanet',
            name='mass_detection_method',
            field=models.CharField(default=b'unk', max_length=3, blank=True, choices=[(b'unk', b'Unknown'), (b'rvs', b'Radial Velocity'), (b'mls', b'Microlensing'), (b'tra', b'Primary Transit'), (b'tim', b'Timing'), (b'ast', b'Astrometry'), (b'img', b'Imaging')]),
        ),
        migrations.AlterField(
            model_name='exoplanet',
            name='radius_detection_method',
            field=models.CharField(default=b'unk', max_length=3, blank=True, choices=[(b'unk', b'Unknown'), (b'rvs', b'Radial Velocity'), (b'mls', b'Microlensing'), (b'tra', b'Primary Transit'), (b'tim', b'Timing'), (b'ast', b'Astrometry'), (b'img', b'Imaging')]),
        ),
    ]
