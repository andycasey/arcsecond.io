# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0006_esoprogrammesummary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='esoprogrammesummary',
            old_name='program_type',
            new_name='programme_type',
        ),
    ]
