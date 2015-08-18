# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0032_auto_20150818_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='FindingChart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input', models.CharField(max_length=100, null=True, blank=True)),
                ('survey_name', models.CharField(default=b'(Undefined)', max_length=10, choices=[(b'(Undefined)', b'(Undefined)'), (b'SDSS', b'SDSS'), (b'SDSS', b'SDSS'), (b'2MASS', b'2MASS')])),
                ('width', models.SmallIntegerField()),
                ('height', models.SmallIntegerField()),
                ('size_unit', models.CharField(default=b'(Undefined)', max_length=10, choices=[(b'(Undefined)', b'(Undefined)'), (b'arcsec', b'arcsec'), (b'arcmin', b'arcmin'), (b'deg', b'deg')])),
                ('orientation', models.CharField(default=b'(Undefined)', max_length=20, choices=[(b'(Undefined)', b'(Undefined)'), (b'N up E left', b'N up E left'), (b'N up E right', b'N up E right'), (b'N down E left', b'N down E left'), (b'N down E right', b'N down E right')])),
                ('band_name', models.CharField(max_length=20, null=True, blank=True)),
                ('fits_url', models.URLField(max_length=500)),
                ('image_url', models.URLField(max_length=500)),
                ('observing_date', models.DateField(null=True, blank=True)),
            ],
        ),
    ]
