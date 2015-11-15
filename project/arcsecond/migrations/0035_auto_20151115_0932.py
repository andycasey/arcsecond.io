# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0034_auto_20151115_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='affiliation',
            name='organisation',
        ),
        migrations.AddField(
            model_name='affiliation',
            name='organisation',
            field=models.ForeignKey(related_name='affiliations', blank=True, to='arcsecond.Organisation', null=True),
        ),
        migrations.RemoveField(
            model_name='affiliation',
            name='person',
        ),
        migrations.AddField(
            model_name='affiliation',
            name='person',
            field=models.ForeignKey(related_name='affiliations', blank=True, to='arcsecond.Person', null=True),
        ),
    ]
