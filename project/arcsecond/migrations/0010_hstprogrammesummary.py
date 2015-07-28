# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0009_esoprogrammesummary_abstract'),
    ]

    operations = [
        migrations.CreateModel(
            name='HSTProgrammeSummary',
            fields=[
                ('programme_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('cycle', models.CharField(max_length=100, null=True, blank=True)),
                ('programme_allocation', models.CharField(max_length=100, null=True, blank=True)),
                ('programme_title', models.CharField(max_length=500)),
                ('programme_principal_investigator', models.CharField(max_length=100)),
                ('programme_pi_institution', models.CharField(max_length=200)),
                ('programme_type', models.CharField(default=b'(Undefined)', max_length=100, choices=[(b'(Undefined)', b'(Undefined)'), (b'Archival Research', b'Archival Research'), (b'Calibration program', b'Calibration program'), (b'Engineering program', b'Engineering program'), (b'General Observer program', b'General Observer program'), (b"Director's Discretionary program", b"Director's Discretionary program"), (b'Pure parallel program', b'Pure parallel program'), (b'Guaranteed Time Observer program', b'Guaranteed Time Observer program'), (b'Observing program conducted at the direction of NASA', b'Observing program conducted at the direction of NASA'), (b'Snapshot program', b'Snapshot program')])),
                ('programme_type_auxiliary', models.CharField(max_length=100)),
                ('programme_status', models.CharField(default=b'(Undefined)', max_length=100, choices=[(b'(Undefined)', b'(Undefined)'), (b'Pending Phase II Submission', b'Pending Phase II Submission'), (b'Implementation', b'Implementation'), (b'Scheduling', b'Scheduling'), (b'Program has been Completed', b'Program has been Completed')])),
                ('programme_abstract', models.CharField(max_length=5000, null=True, blank=True)),
                ('related_programmes', models.ForeignKey(blank=True, to='arcsecond.HSTProgrammeSummary', null=True)),
            ],
        ),
    ]
