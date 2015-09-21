# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0008_auto_20150921_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observingsiteactivity',
            name='action_message',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='observingsiteactivity',
            name='new_value',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='observingsiteactivity',
            name='old_value',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='observingsiteactivity',
            name='property_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
