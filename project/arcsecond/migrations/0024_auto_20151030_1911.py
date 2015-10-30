# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0023_auto_20151030_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observingsiteactivity',
            name='user',
            field=models.ForeignKey(related_name='observingsite_activities', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
