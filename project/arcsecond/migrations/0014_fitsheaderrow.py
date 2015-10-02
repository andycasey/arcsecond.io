# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0013_esoarchivedatarow_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='FITSHeaderRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=100, null=True, blank=True)),
                ('value', models.CharField(max_length=100, null=True, blank=True)),
                ('comment', models.CharField(max_length=100, null=True, blank=True)),
                ('data_row', models.ForeignKey(related_name='header_rows', blank=True, to='arcsecond.ESOArchiveDataRow', null=True)),
            ],
        ),
    ]
