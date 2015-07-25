# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0005_auto_20150722_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='ESOProgrammeSummary',
            fields=[
                ('programme_id', models.CharField(max_length=20, serialize=False, primary_key=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{2,3}\\.[A-Fa-f]{1}-[0-9]{4}\\([A-Za-z]{1}\\)', message=b'Invalid ESO Programme ID', code=b'nomatch')])),
                ('period', models.CharField(max_length=100, null=True, blank=True)),
                ('observing_mode', models.CharField(default=b'(Undefined)', max_length=100, choices=[(b'(Undefined)', b'(Undefined)'), (b'Visitor', b'Visitor'), (b'Service', b'Service')])),
                ('program_type', models.CharField(default=b'(Undefined)', max_length=100, choices=[(b'(Undefined)', b'(Undefined)'), (b'Normal Programme', b'Normal Programme'), (b'Guaranteed Time Observations', b'Guaranteed Time Observations'), (b"Director's Discretionary Time", b"Director's Discretionary Time"), (b'Target of Opportunity', b'Target of Opportunity'), (b'Large Programme', b'Large Programme'), (b'Short Programme', b'Short Programme'), (b'Calibration Programme', b'Calibration Programme'), (b'Monitoring Programme', b'Monitoring Programme')])),
                ('allocated_time', models.CharField(max_length=100, null=True, blank=True)),
                ('telescope_name', models.CharField(max_length=100, null=True, blank=True)),
                ('instrument_name', models.CharField(max_length=100, null=True, blank=True)),
                ('investigators_list', models.CharField(max_length=500, null=True, blank=True)),
                ('proposal_title', models.CharField(max_length=500, null=True, blank=True)),
                ('remarks', models.CharField(max_length=500, null=True, blank=True)),
                ('abstract_url', models.URLField(max_length=500, null=True, blank=True)),
                ('observer_name', models.CharField(max_length=500, null=True, blank=True)),
                ('raw_files_url', models.URLField(max_length=500, null=True, blank=True)),
                ('publications_url', models.URLField(max_length=500, null=True, blank=True)),
            ],
        ),
    ]
