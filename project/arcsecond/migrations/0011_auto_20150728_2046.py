# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0010_hstprogrammesummary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hstprogrammesummary',
            old_name='programme_abstract',
            new_name='abstract',
        ),
        migrations.RenameField(
            model_name='hstprogrammesummary',
            old_name='programme_allocation',
            new_name='allocation',
        ),
        migrations.RenameField(
            model_name='hstprogrammesummary',
            old_name='programme_pi_institution',
            new_name='pi_institution',
        ),
        migrations.RenameField(
            model_name='hstprogrammesummary',
            old_name='programme_principal_investigator',
            new_name='principal_investigator',
        ),
        migrations.RenameField(
            model_name='hstprogrammesummary',
            old_name='programme_title',
            new_name='title',
        ),
    ]
