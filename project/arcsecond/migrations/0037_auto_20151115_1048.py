# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0036_publication_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='publication_date',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
    ]
