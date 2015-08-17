# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0029_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimesConversion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input_value', models.CharField(max_length=100, null=True, blank=True)),
                ('documentation_URL', models.URLField(null=True, blank=True)),
                ('byear', models.FloatField(max_length=100, null=True, blank=True)),
                ('byear_str', models.CharField(max_length=100, null=True, blank=True)),
                ('cxcsec', models.FloatField(max_length=100, null=True, blank=True)),
                ('datetime', models.CharField(max_length=100, null=True, blank=True)),
                ('decimalyear', models.FloatField(max_length=100, null=True, blank=True)),
                ('gps', models.FloatField(max_length=100, null=True, blank=True)),
                ('iso', models.CharField(max_length=100, null=True, blank=True)),
                ('isot', models.CharField(max_length=100, null=True, blank=True)),
                ('jd', models.FloatField(max_length=100, null=True, blank=True)),
                ('jyear', models.FloatField(max_length=100, null=True, blank=True)),
                ('jyear_str', models.CharField(max_length=100, null=True, blank=True)),
                ('mjd', models.FloatField(max_length=100, null=True, blank=True)),
                ('plot_date', models.FloatField(max_length=100, null=True, blank=True)),
                ('unix', models.FloatField(max_length=100, null=True, blank=True)),
                ('yday', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
    ]
