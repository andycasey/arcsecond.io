# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0025_auto_20150813_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='publication_type',
            field=models.CharField(default=b'unk', max_length=3, choices=[(b'unk', b'unknown'), (b'art', b'article')]),
        ),
        migrations.AlterField(
            model_name='age',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='albedo',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='angle',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='color',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='distance',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='eccentricity',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='ellipseaxis',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='flux',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='gravity',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='julianday',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='mass',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='metallicity',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='period',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='publication',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='radius',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='velocity',
            name='bibcode',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
    ]
