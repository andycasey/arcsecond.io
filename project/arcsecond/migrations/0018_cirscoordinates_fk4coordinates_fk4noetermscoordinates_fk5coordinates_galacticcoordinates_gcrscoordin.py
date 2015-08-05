# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0017_coordinatesconversion'),
    ]

    operations = [
        migrations.CreateModel(
            name='CIRSCoordinates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ra', models.CharField(max_length=20, null=True, blank=True)),
                ('ra_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('dec', models.CharField(max_length=20, null=True, blank=True)),
                ('dec_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('distance', models.CharField(max_length=20, null=True, blank=True)),
                ('distance_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('documentation', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FK4Coordinates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ra', models.CharField(max_length=20, null=True, blank=True)),
                ('ra_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('dec', models.CharField(max_length=20, null=True, blank=True)),
                ('dec_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('distance', models.CharField(max_length=20, null=True, blank=True)),
                ('distance_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('equinox', models.CharField(max_length=20, null=True, blank=True)),
                ('documentation', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FK4NoETermsCoordinates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ra', models.CharField(max_length=20, null=True, blank=True)),
                ('ra_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('dec', models.CharField(max_length=20, null=True, blank=True)),
                ('dec_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('distance', models.CharField(max_length=20, null=True, blank=True)),
                ('distance_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('equinox', models.CharField(max_length=20, null=True, blank=True)),
                ('documentation', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FK5Coordinates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ra', models.CharField(max_length=20, null=True, blank=True)),
                ('ra_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('dec', models.CharField(max_length=20, null=True, blank=True)),
                ('dec_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('distance', models.CharField(max_length=20, null=True, blank=True)),
                ('distance_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('equinox', models.CharField(max_length=20, null=True, blank=True)),
                ('documentation', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GalacticCoordinates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('l', models.CharField(max_length=20, null=True, blank=True)),
                ('l_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('b', models.CharField(max_length=20, null=True, blank=True)),
                ('b_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('distance', models.CharField(max_length=20, null=True, blank=True)),
                ('distance_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('documentation', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GCRSCoordinates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ra', models.CharField(max_length=20, null=True, blank=True)),
                ('ra_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('dec', models.CharField(max_length=20, null=True, blank=True)),
                ('dec_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('distance', models.CharField(max_length=20, null=True, blank=True)),
                ('distance_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('documentation', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ICRSCoordinates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ra', models.CharField(max_length=20, null=True, blank=True)),
                ('ra_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('dec', models.CharField(max_length=20, null=True, blank=True)),
                ('dec_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('distance', models.CharField(max_length=20, null=True, blank=True)),
                ('distance_unit', models.CharField(max_length=20, null=True, blank=True)),
                ('documentation', models.URLField(null=True, blank=True)),
            ],
        ),
    ]
