# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0039_auto_20150831_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='coordinates',
            field=models.ManyToManyField(related_name='building', to='arcsecond.Coordinates', blank=True),
        ),
    ]
