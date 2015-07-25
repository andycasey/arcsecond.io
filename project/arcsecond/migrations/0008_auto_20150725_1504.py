# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0007_auto_20150725_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='esoprogrammesummary',
            old_name='proposal_title',
            new_name='programme_title',
        ),
    ]
