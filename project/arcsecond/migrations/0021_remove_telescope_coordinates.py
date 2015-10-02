# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0020_telescope_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telescope',
            name='coordinates',
        ),
    ]
