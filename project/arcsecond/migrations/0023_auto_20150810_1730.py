# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0022_auto_20150810_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='astronomerstelegram',
            name='authors',
            field=models.ManyToManyField(related_name='astronomer_telegrams', to='arcsecond.Person'),
        ),
        migrations.AddField(
            model_name='astronomerstelegram',
            name='credential_certification',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='astronomerstelegram',
            name='detected_objects',
            field=models.ManyToManyField(related_name='astronomer_telegrams', to='arcsecond.AstronomicalObject'),
        ),
        migrations.AddField(
            model_name='astronomerstelegram',
            name='subjects',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
