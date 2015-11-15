# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0032_auto_20151110_0713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='affiliations',
        ),
        migrations.AddField(
            model_name='publisher',
            name='acronym',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='bibcode',
            field=models.CharField(unique=True, max_length=50, validators=[django.core.validators.RegexValidator(regex=b'[0-9]{4}[A-Za-z&]+[\\.]*[0-9]+[A-Za-z]?[\\.]*[0-9]+[A-Z]', message=b'Invalid bibcode', code=b'nomatch')]),
        ),
        migrations.AlterField(
            model_name='publication',
            name='publication_type',
            field=models.CharField(default=b'unk', max_length=5, choices=[(b'unk', b'unknown'), (b'art', b'article'), (b'proc', b'proceedings'), (b'prop', b'proposal'), (b'prep', b'preprint')]),
        ),
    ]
