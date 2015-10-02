# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0021_remove_telescope_coordinates'),
    ]

    operations = [
        migrations.AddField(
            model_name='telescope',
            name='image_url_copyright',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
