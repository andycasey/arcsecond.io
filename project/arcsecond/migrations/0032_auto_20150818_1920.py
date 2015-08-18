# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0031_timesconversion_input_format'),
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.PositiveSmallIntegerField()),
                ('message', models.CharField(max_length=1000, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='coordinatesconversion',
            name='error',
            field=models.OneToOneField(related_name='coordinates_conversion_error', null=True, blank=True, to='arcsecond.Error'),
        ),
        migrations.AddField(
            model_name='timesconversion',
            name='error',
            field=models.OneToOneField(related_name='times_conversion_error', null=True, blank=True, to='arcsecond.Error'),
        ),
    ]
