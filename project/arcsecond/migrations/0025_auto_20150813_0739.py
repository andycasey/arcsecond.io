# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0024_auto_20150813_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='publications',
            field=models.ForeignKey(related_name='download_links', blank=True, to='arcsecond.Publication', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='profile_URL',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='abstract',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='abstract_copyright',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='bibtex_entry',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='citations',
            field=models.ManyToManyField(related_name='citations_rel_+', to='arcsecond.Publication'),
        ),
        migrations.AddField(
            model_name='publication',
            name='doi',
            field=models.OneToOneField(related_name='doi', null=True, blank=True, to='arcsecond.Link'),
        ),
        migrations.AddField(
            model_name='publication',
            name='first_page_number',
            field=models.IntegerField(default=-1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='is_refereed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='issue_number',
            field=models.IntegerField(default=-1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='journal_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='keywords',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='number_of_pages',
            field=models.IntegerField(default=-1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='origin',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='publication_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='references',
            field=models.ManyToManyField(related_name='references_rel_+', to='arcsecond.Publication'),
        ),
        migrations.AddField(
            model_name='publication',
            name='related_objects',
            field=models.ManyToManyField(related_name='related_objects', to='arcsecond.AstronomicalObject'),
        ),
        migrations.AddField(
            model_name='publication',
            name='subjects',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='volume_number',
            field=models.IntegerField(default=-1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='authors',
            field=models.ManyToManyField(related_name='publications', to='arcsecond.Person'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(default=b'', max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='year',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
