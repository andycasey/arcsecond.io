# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0035_auto_20150818_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='findingchart',
            name='height',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='findingchart',
            name='orientation',
            field=models.CharField(default=b'unk', max_length=20, choices=[(b'unk', b'(Undefined)'), (b'NuEl', b'N up E left'), (b'NuEr', b'N up E right'), (b'NdEl', b'N down E left'), (b'NdEr', b'N down E right')]),
        ),
        migrations.AlterField(
            model_name='findingchart',
            name='size_unit',
            field=models.CharField(default=b'unk', max_length=20, choices=[(b'unk', b'(Undefined)'), (b'arcsec', b'arcseconds'), (b'arcmin', b'arcminutes'), (b'deg', b'degrees')]),
        ),
        migrations.AlterField(
            model_name='findingchart',
            name='survey_name',
            field=models.CharField(default=b'unk', max_length=20, choices=[(b'unk', b'(Undefined)'), (b'sdss', b'SDSS'), (b'dss', b'DSS'), (b'2mass', b'2MASS')]),
        ),
        migrations.AlterField(
            model_name='findingchart',
            name='width',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
