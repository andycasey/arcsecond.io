# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arcsecond', '0037_findingchart_astronomical_object'),
    ]

    operations = [
        migrations.AddField(
            model_name='mirror',
            name='mirror_index',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='telescope',
            name='has_active_optics',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='telescope',
            name='has_adaptative_optics',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='telescope',
            name='has_laser_guide_star',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='mirror',
            name='coating',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mirror',
            name='curvature',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mirror',
            name='material',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mirror',
            name='shape',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='telescope',
            name='mounting',
            field=models.CharField(default=b'unk', max_length=3, blank=True, choices=[(b'unk', b'Unknown'), (b'equ', b'EquatorialCassegrain'), (b'cas', b'Alt-Az'), (b'aaz', b'Off-Axis')]),
        ),
        migrations.AlterField(
            model_name='telescope',
            name='optical_design',
            field=models.CharField(default=b'unk', max_length=3, blank=True, choices=[(b'unk', 'Unknown'), (b'rc', 'Ritchey-Chr\xe9tien'), (b'sc', 'Schmidt')]),
        ),
        migrations.AlterField(
            model_name='toolcomponent',
            name='name',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
    ]
