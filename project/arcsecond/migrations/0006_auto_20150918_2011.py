# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0005_auto_20150918_2011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observingsite',
            old_name='long_name',
            new_name='name',
        ),
    ]
