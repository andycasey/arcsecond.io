# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iobserve', '0002_auto_20150601_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('warn', models.CharField(default=b'', max_length=1000)),
                ('error', models.CharField(default=b'', max_length=1000)),
                ('info', models.CharField(default=b'', max_length=1000)),
                ('debug', models.CharField(default=b'', max_length=1000)),
                ('http_status_code', models.IntegerField(default=0)),
            ],
        ),
    ]
