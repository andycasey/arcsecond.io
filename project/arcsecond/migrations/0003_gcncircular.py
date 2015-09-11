# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0002_auto_20150909_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='GCNCircular',
            fields=[
                ('identifier', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=1000, null=True, blank=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('content', models.CharField(max_length=20000, null=True, blank=True)),
                ('authors', models.ManyToManyField(related_name='GCN_circulars', to='arcsecond.Person')),
                ('detected_objects', models.ManyToManyField(related_name='GCN_circulars', to='arcsecond.AstronomicalObject')),
                ('external_links', models.ManyToManyField(related_name='GCN_circulars', to='arcsecond.Link')),
                ('related_circulars', models.ManyToManyField(related_name='related_circulars_rel_+', to='arcsecond.GCNCircular')),
                ('submitter', models.ForeignKey(related_name='submitted_GCN_circulars', to='arcsecond.Person')),
            ],
        ),
    ]
