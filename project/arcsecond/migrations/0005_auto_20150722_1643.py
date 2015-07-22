# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0004_auto_20150719_0754'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.AlterField(
            model_name='observingsite',
            name='continent',
            field=models.CharField(default=b'(Undefined)', max_length=100, choices=[(b'(Undefined)', b'(Undefined)'), (b'Asia', b'Asia'), (b'Africa', b'Africa'), (b'Antarctica', b'Antarctica'), (b'Europe', b'Europe'), (b'North America', b'North America'), (b'Oceania', b'Oceania'), (b'South America', b'South America')]),
        ),
    ]
