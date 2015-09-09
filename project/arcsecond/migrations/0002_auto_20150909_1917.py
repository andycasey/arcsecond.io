# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telescope',
            name='mounting',
            field=models.CharField(default=b'unk', max_length=3, blank=True, choices=[(b'unk', b'Unknown'), (b'equ', b'Equatorial'), (b'cas', b'Cassegrain'), (b'aaz', b'Alt-Az'), (b'off', b'Off-Axis')]),
        ),
    ]
