# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0012_auto_20150731_2025'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Parallax',
        ),
        migrations.AlterField(
            model_name='age',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='age',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='age',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='age',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='age',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='albedo',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='albedo',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='albedo',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='albedo',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='albedo',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='angle',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='angle',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='angle',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='angle',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='angle',
            name='unit',
            field=models.CharField(default=b'sec', max_length=3, choices=[(b'mas', b'mas'), (b'sec', b"'"), (b'min', b'"'), (b'deg', '\xba')]),
        ),
        migrations.AlterField(
            model_name='angle',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='color',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='distance',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='distance',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='distance',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='distance',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='distance',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eccentricity',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='eccentricity',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eccentricity',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eccentricity',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eccentricity',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ellipseaxis',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='ellipseaxis',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ellipseaxis',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ellipseaxis',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ellipseaxis',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='exoplanet',
            name='angular_distance',
            field=models.OneToOneField(related_name='angular_distance', null=True, blank=True, to='arcsecond.Angle'),
        ),
        migrations.AlterField(
            model_name='flux',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='flux',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flux',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flux',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flux',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gravity',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='gravity',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gravity',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gravity',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gravity',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='julianday',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='julianday',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='julianday',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='julianday',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='julianday',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mass',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='mass',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mass',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mass',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mass',
            name='unit',
            field=models.CharField(default=b'sun', max_length=3, choices=[(b'sun', b'Sun'), (b'jup', b'Jupiter'), (b'nep', b'Neptune'), (b'ear', b'Earth')]),
        ),
        migrations.AlterField(
            model_name='mass',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='metallicity',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='metallicity',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='metallicity',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='metallicity',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='metallicity',
            name='unit',
            field=models.CharField(default=b'Z', max_length=1, choices=[(b'Z', b'Z'), (b'F', b'Fe/H')]),
        ),
        migrations.AlterField(
            model_name='metallicity',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='period',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='period',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='period',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='period',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='period',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='radius',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='radius',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='radius',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='radius',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='radius',
            name='unit',
            field=models.CharField(default=b'sun', max_length=3, choices=[(b'sun', b'Sun'), (b'jup', b'Jupiter'), (b'nep', b'Neptune'), (b'ear', b'Earth')]),
        ),
        migrations.AlterField(
            model_name='radius',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='velocity',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='velocity',
            name='error',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='velocity',
            name='error_max',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='velocity',
            name='error_min',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='velocity',
            name='value',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='AngularDistance',
        ),
    ]
