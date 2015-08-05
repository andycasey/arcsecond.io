# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0020_auto_20150805_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='cirscoordinates',
            name='documentation_URL',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fk4coordinates',
            name='documentation_URL',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fk4noetermscoordinates',
            name='documentation_URL',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fk5coordinates',
            name='documentation_URL',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='galacticcoordinates',
            name='documentation_URL',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='gcrscoordinates',
            name='documentation_URL',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='icrscoordinates',
            name='documentation_URL',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cirscoordinates',
            name='documentation',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fk4coordinates',
            name='documentation',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fk4noetermscoordinates',
            name='documentation',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fk5coordinates',
            name='documentation',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='galacticcoordinates',
            name='documentation',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gcrscoordinates',
            name='documentation',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='icrscoordinates',
            name='documentation',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
