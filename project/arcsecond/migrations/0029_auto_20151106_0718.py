# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0028_auto_20151106_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observingsite',
            name='sources',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=100, null=True, choices=[(b'(Undefined)', b'(Undefined)'), (b'User', b'User'), (b'iObserve', b'iObserve'), (b'Xephem', b'Xephem'), (b'MPC', b'MPC')]),
        ),
    ]
