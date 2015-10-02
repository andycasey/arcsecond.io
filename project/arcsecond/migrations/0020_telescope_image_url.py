# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0019_esoarchivedatarow_exposure_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='telescope',
            name='image_url',
            field=models.URLField(max_length=500, null=True, blank=True),
        ),
    ]
