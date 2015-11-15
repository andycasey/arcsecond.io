# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0029_auto_20151106_0718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='profile_URL',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='bibtex_entry',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='journal_name',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='origin',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='subjects',
        ),
        migrations.AddField(
            model_name='person',
            name='initials',
            field=django.contrib.postgres.fields.ArrayField(default=list, base_field=models.CharField(max_length=10, null=True, blank=True), size=None),
        ),
        migrations.AddField(
            model_name='publication',
            name='keywords_tmp',
            field=django.contrib.postgres.fields.ArrayField(default=list, base_field=models.CharField(max_length=100, null=True, blank=True), size=None),
        ),
        migrations.AddField(
            model_name='publication',
            name='subjects_tmp',
            field=django.contrib.postgres.fields.ArrayField(default=list, base_field=models.CharField(max_length=200, null=True, blank=True), size=None),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='middle_name',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='is_refereed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='publication',
            name='publication_type',
            field=models.CharField(default=b'unk', max_length=5, choices=[(b'unk', b'unknown'), (b'art', b'article'), (b'proc', b'proceedings'), (b'prop', b'proposal')]),
        ),
        migrations.AddField(
            model_name='affiliation',
            name='organisation',
            field=models.ManyToManyField(related_name='organisation_affiliations', to='arcsecond.Person', blank=True),
        ),
        migrations.AddField(
            model_name='affiliation',
            name='person',
            field=models.ManyToManyField(related_name='affiliations', to='arcsecond.Person', blank=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='affiliations',
            field=models.ManyToManyField(related_name='publications', to='arcsecond.Organisation'),
        ),
        migrations.AddField(
            model_name='publication',
            name='journal',
            field=models.ForeignKey(related_name='publications', blank=True, to='arcsecond.Publisher', null=True),
        ),
    ]
