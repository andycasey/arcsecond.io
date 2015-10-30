# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0022_telescope_image_url_copyright'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observingsiteactivity',
            name='observing_site',
            field=models.ForeignKey(related_name='activities', blank=True, to='arcsecond.ObservingSite', null=True),
        ),
        migrations.AlterField(
            model_name='observingsiteactivity',
            name='user',
            field=models.ForeignKey(related_name='activities', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
