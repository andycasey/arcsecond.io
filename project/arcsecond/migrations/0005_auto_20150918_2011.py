# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0004_auto_20150911_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observingsite',
            old_name='name',
            new_name='short_name',
        ),
        migrations.AddField(
            model_name='observingsite',
            name='alternate_name_1',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='observingsite',
            name='alternate_name_2',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='observingsite',
            name='state_province',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
