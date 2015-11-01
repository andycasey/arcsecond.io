# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0025_userprofile_membership_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observingsite',
            name='coordinates',
            field=models.OneToOneField(related_name='site', null=True, to='arcsecond.Coordinates'),
        ),
    ]
