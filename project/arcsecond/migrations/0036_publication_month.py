# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0035_auto_20151115_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='month',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
