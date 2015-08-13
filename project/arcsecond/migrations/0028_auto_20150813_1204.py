# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0027_auto_20150813_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='eprintid',
            new_name='eprint_id',
        ),
        migrations.AlterField(
            model_name='publication',
            name='publication_type',
            field=models.CharField(default=b'unk', max_length=3, choices=[(b'unk', b'unknown'), (b'art', b'article'), (b'proc', b'proceedings')]),
        ),
    ]
