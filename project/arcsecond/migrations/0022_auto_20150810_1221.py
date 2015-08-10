# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0021_auto_20150805_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='AstronomersTelegram',
            fields=[
                ('identifier', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=1000, null=True, blank=True)),
                ('content', models.CharField(max_length=20000, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1000, null=True, blank=True)),
                ('url', models.URLField(max_length=2000, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='astronomerstelegram',
            name='external_links',
            field=models.ManyToManyField(related_name='astronomer_telegrams', to='arcsecond.Link'),
        ),
        migrations.AddField(
            model_name='astronomerstelegram',
            name='related_telegrams',
            field=models.ManyToManyField(related_name='related_telegrams_rel_+', to='arcsecond.AstronomersTelegram'),
        ),
    ]
