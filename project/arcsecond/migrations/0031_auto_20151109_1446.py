# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0030_auto_20151109_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='keywords_tmp',
            new_name='keywords',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='subjects_tmp',
            new_name='subjects',
        ),
    ]
