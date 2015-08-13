# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0026_auto_20150813_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='eprintid',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='first_page_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='issue_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='number_of_pages',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='volume_number',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
