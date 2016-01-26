# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0038_auto_20151213_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='astronomerstelegram',
            name='referring_telegrams',
            field=models.ManyToManyField(related_name='referring_telegrams_rel_+', to='arcsecond.AstronomersTelegram'),
        ),
    ]
