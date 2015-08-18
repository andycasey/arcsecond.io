# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0033_findingchart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='findingchart',
            name='size_unit',
            field=models.CharField(default=b'(Undefined)', max_length=20, choices=[(b'(Undefined)', b'(Undefined)'), (b'arcsec', b'arcsec'), (b'arcmin', b'arcmin'), (b'deg', b'deg')]),
        ),
        migrations.AlterField(
            model_name='findingchart',
            name='survey_name',
            field=models.CharField(default=b'(Undefined)', max_length=20, choices=[(b'(Undefined)', b'(Undefined)'), (b'SDSS', b'SDSS'), (b'SDSS', b'SDSS'), (b'2MASS', b'2MASS')]),
        ),
    ]
