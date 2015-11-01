# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0026_auto_20151031_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observingsiteactivity',
            name='action',
            field=models.CharField(default=b'unk', max_length=10, choices=[(b'unk', b'(Undefined)'), (b'load', b'loaded'), (b'prop', b'changed property'), (b'del', b'deleted site'), (b'cre', b'created site')]),
        ),
    ]
