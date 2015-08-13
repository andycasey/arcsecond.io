# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0023_auto_20150810_1730'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BibliographicReference',
            new_name='Publication',
        ),
    ]
