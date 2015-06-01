# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('catalogue_url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AstronomicalCoordinates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('right_ascension', models.FloatField(default=-9999999999999)),
                ('right_ascension_units', models.CharField(default=b'degrees', max_length=100)),
                ('declination', models.FloatField(default=-9999999999999)),
                ('declination_units', models.CharField(default=b'degrees', max_length=100)),
                ('epoch', models.FloatField(default=2000)),
                ('equinox', models.FloatField(default=2000)),
            ],
        ),
        migrations.CreateModel(
            name='AstronomicalFlux',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('value', models.FloatField(default=-9999999999999)),
                ('error_value', models.FloatField(default=-9999999999999)),
                ('bibcode', models.CharField(max_length=500, null=True, blank=True)),
                ('unit', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AstronomicalObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('coordinates', models.OneToOneField(null=True, to='iobserve.AstronomicalCoordinates')),
            ],
        ),
        migrations.CreateModel(
            name='AstronomicalOrganisation',
            fields=[
                ('name', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('acronym', models.CharField(max_length=100, null=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('wikipedia_article', models.URLField(null=True, blank=True)),
                ('organisation_type', models.CharField(default=b'Unknown', max_length=100, choices=[(b'Unknown', b'Unknown'), (b'Public', b'Public'), (b'Private', b'Private'), (b'Mixed', b'Mixed')])),
            ],
        ),
        migrations.CreateModel(
            name='BibliographicReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1000)),
                ('year', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('name', models.CharField(max_length=1000, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('longitude', models.FloatField(default=-9999999999999)),
                ('latitude', models.FloatField(default=-9999999999999)),
                ('height', models.FloatField(default=-9999999999999)),
            ],
            options={
                'ordering': ['longitude', 'latitude'],
            },
        ),
        migrations.CreateModel(
            name='ObjectType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=500)),
                ('astronomical_object', models.ForeignKey(related_name='object_types', blank=True, to='iobserve.AstronomicalObject', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ObservingSite',
            fields=[
                ('name', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('long_name', models.CharField(max_length=100, null=True, blank=True)),
                ('IAUCode', models.CharField(max_length=200, null=True, blank=True)),
                ('continent', models.CharField(default=b'(Undefined)', max_length=100, choices=[(b'(Undefined)', b'(Undefined)'), (b'Asia', b'Asia'), (b'Antarctica', b'Antarctica'), (b'Europe', b'Europe'), (b'North America', b'North America'), (b'Oceania', b'Oceania'), (b'South America', b'South America')])),
                ('address_line_1', models.CharField(max_length=200, null=True, blank=True)),
                ('address_line_2', models.CharField(max_length=200, null=True, blank=True)),
                ('zip_code', models.IntegerField(null=True, blank=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('time_zone', models.CharField(max_length=200, null=True, blank=True)),
                ('time_zone_name', models.CharField(max_length=200, null=True, blank=True)),
                ('homepage', models.URLField(null=True, blank=True)),
                ('wikipedia_article', models.URLField(null=True, blank=True)),
                ('coordinates', models.OneToOneField(related_name='site', to='iobserve.Coordinates')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=1000)),
                ('middle_name', models.CharField(max_length=1000)),
                ('last_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('name', models.CharField(max_length=1000, serialize=False, primary_key=True)),
                ('acronym', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ToolComponent',
            fields=[
                ('name', models.CharField(max_length=1000, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
        migrations.CreateModel(
            name='Dome',
            fields=[
                ('building_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='iobserve.Building')),
            ],
            bases=('iobserve.building',),
        ),
        migrations.CreateModel(
            name='Mirror',
            fields=[
                ('toolcomponent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='iobserve.ToolComponent')),
                ('diameter', models.FloatField(null=True, blank=True)),
                ('thickness', models.FloatField(null=True, blank=True)),
                ('shape', models.CharField(max_length=1000, null=True, blank=True)),
                ('curvature', models.CharField(max_length=1000, null=True, blank=True)),
                ('coating', models.CharField(max_length=1000, null=True, blank=True)),
                ('central_obscuration', models.FloatField(null=True, blank=True)),
                ('material', models.CharField(max_length=1000, null=True, blank=True)),
                ('creation_date', models.DateField(null=True, blank=True)),
            ],
            bases=('iobserve.toolcomponent',),
        ),
        migrations.CreateModel(
            name='ObservingTool',
            fields=[
                ('tool_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='iobserve.Tool')),
            ],
            bases=('iobserve.tool',),
        ),
        migrations.AlterUniqueTogether(
            name='coordinates',
            unique_together=set([('longitude', 'latitude')]),
        ),
        migrations.AddField(
            model_name='building',
            name='coordinates',
            field=models.ManyToManyField(related_name='building', to='iobserve.Coordinates', blank=True),
        ),
        migrations.AddField(
            model_name='astronomicalorganisation',
            name='headquarters',
            field=models.OneToOneField(related_name='astronomical_organisation', null=True, blank=True, to='iobserve.ObservingSite'),
        ),
        migrations.AddField(
            model_name='astronomicalorganisation',
            name='observing_sites',
            field=models.ManyToManyField(related_name='astronomical_organisations', to='iobserve.ObservingSite'),
        ),
        migrations.AddField(
            model_name='astronomicalflux',
            name='astronomical_object',
            field=models.ForeignKey(related_name='fluxes', blank=True, to='iobserve.AstronomicalObject', null=True),
        ),
        migrations.AddField(
            model_name='alias',
            name='astronomical_object',
            field=models.ForeignKey(related_name='aliases', blank=True, to='iobserve.AstronomicalObject', null=True),
        ),
        migrations.CreateModel(
            name='Telescope',
            fields=[
                ('observingtool_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='iobserve.ObservingTool')),
                ('wavelength_domains', multiselectfield.db.fields.MultiSelectField(max_length=51, choices=[(b'hga', b'Hard gamma-rays'), (b'wga', b'Weak gamma-rays'), (b'hxr', b'Hard x-rays'), (b'wxr', b'Weak x-rays'), (b'fuv', b'Far ultraviolet'), (b'nuv', b'Near ultraviolet'), (b'opt', b'Optical'), (b'nir', b'Near infrared'), (b'mir', b'Mid-infrared'), (b'fir', b'Far infrared'), (b'smm', b'Sub-milimetric'), (b'mmc', b'Milimetric'), (b'rad', b'Radio')])),
                ('mounting', models.CharField(max_length=3, choices=[(b'equ', b'Equatorial'), (b'cas', b'Cassegrain'), (b'aaz', b'Alt-Az')])),
                ('optical_design', models.CharField(blank=True, max_length=2, null=True, choices=[(b'rc', 'Ritchey-Chretien'), (b'sc', 'Schmidt')])),
                ('dome', models.OneToOneField(related_name='telescope', null=True, default=None, blank=True, to='iobserve.Dome')),
            ],
            bases=('iobserve.observingtool',),
        ),
        migrations.AddField(
            model_name='observingtool',
            name='coordinates',
            field=models.ManyToManyField(related_name='observing_tool', to='iobserve.Coordinates'),
        ),
        migrations.AddField(
            model_name='mirror',
            name='telescope',
            field=models.ForeignKey(related_name='mirrors', default=None, blank=True, to='iobserve.Telescope', null=True),
        ),
    ]
