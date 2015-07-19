# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('unit', models.CharField(default=b'Gyr', max_length=3, choices=[(b'Gyr', b'Gyr'), (b'Myr', b'Myr'), (b'yr', b'yr')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Albedo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('catalogue_url', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Angle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('unit', models.CharField(default=b'degrees', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AngularDistance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('unit', models.CharField(default=b's', max_length=1, choices=[(b's', b'arcsec'), (b'mn', b'arcmin')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AstronomicalCoordinates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('system', models.CharField(default=b'ICRS', max_length=20, choices=[(b'ICRS', b'ICRS'), (b'FK5', b'FK5'), (b'FK4', b'FK4'), (b'FK4NoETerms', b'FK4NoETerms'), (b'Galactic', b'Galactic'), (b'AltAz', b'AltAz')])),
                ('right_ascension', models.FloatField(default=-9999999999999)),
                ('right_ascension_units', models.CharField(default=b'degrees', max_length=100)),
                ('declination', models.FloatField(default=-9999999999999)),
                ('declination_units', models.CharField(default=b'degrees', max_length=100)),
                ('epoch', models.FloatField(default=2000)),
                ('equinox', models.FloatField(default=2000)),
            ],
        ),
        migrations.CreateModel(
            name='AstronomicalObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('coordinates', models.OneToOneField(null=True, blank=True, to='arcsecond.AstronomicalCoordinates')),
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
                ('title', models.CharField(default=b'', max_length=1000)),
                ('year', models.IntegerField(default=0)),
                ('bibcode', models.CharField(default=b'', max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('name', models.CharField(max_length=1000, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('first_magnitude_name', models.CharField(max_length=2)),
                ('second_magnitude_name', models.CharField(max_length=2)),
            ],
            options={
                'abstract': False,
            },
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
            name='Distance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('unit', models.CharField(default=b'pc', max_length=3, choices=[(b'km', b'km'), (b'UA', b'UA'), (b'ly', b'ly'), (b'pc', b'pc'), (b'kpc', b'kpc'), (b'Mpc', b'Mpc')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Eccentricity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EllipseAxis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('unit', models.CharField(default=b'UA', max_length=4, choices=[(b'UA', b'UA'), (b'Rsun', b'Rsun')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exoplanet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('discovery_date', models.DateField(null=True, blank=True)),
                ('last_update', models.DateField(null=True, blank=True)),
                ('molecules_detected', models.CharField(max_length=100)),
                ('detection_method', models.CharField(default=b'unk', max_length=3, blank=True, choices=[(b'unk', b'unknown'), (b'rvs', b'radial velocities'), (b'mls', b'microlensing'), (b'tra', b'transit'), (b'tim', b'timing'), (b'ast', b'astrometry'), (b'img', b'imaging')])),
                ('mass_detection_method', models.CharField(default=b'unk', max_length=3, blank=True, choices=[(b'unk', b'unknown'), (b'rvs', b'radial velocities'), (b'mls', b'microlensing'), (b'tra', b'transit'), (b'tim', b'timing'), (b'ast', b'astrometry'), (b'img', b'imaging')])),
                ('radius_detection_method', models.CharField(default=b'unk', max_length=3, blank=True, choices=[(b'unk', b'unknown'), (b'rvs', b'radial velocities'), (b'mls', b'microlensing'), (b'tra', b'transit'), (b'tim', b'timing'), (b'ast', b'astrometry'), (b'img', b'imaging')])),
                ('anomaly_angle', models.OneToOneField(related_name='anomaly_angle', null=True, blank=True, to='arcsecond.Angle')),
            ],
        ),
        migrations.CreateModel(
            name='Flux',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('name', models.CharField(max_length=500)),
                ('astronomical_object', models.ForeignKey(related_name='fluxes', blank=True, to='arcsecond.AstronomicalObject', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gravity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('unit', models.CharField(default=b'log(g/gH)', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JulianDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('unit', models.CharField(default=b'sun', max_length=3, choices=[(b'sun', b'Sun'), (b'jup', b'Jupiter'), (b'nep', b'Neptune'), (b'eee', b'Earth')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('warn', models.CharField(default=b'', max_length=1000)),
                ('error', models.CharField(default=b'', max_length=1000)),
                ('info', models.CharField(default=b'', max_length=1000)),
                ('debug', models.CharField(default=b'', max_length=1000)),
                ('http_status_code', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Metallicity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('unit', models.CharField(default=b'Z', max_length=4, choices=[(b'Z', b'Z'), (b'F', b'Fe/H')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ObjectType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=500)),
                ('astronomical_object', models.ForeignKey(related_name='object_types', blank=True, to='arcsecond.AstronomicalObject', null=True)),
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
                ('coordinates', models.OneToOneField(related_name='site', to='arcsecond.Coordinates')),
            ],
        ),
        migrations.CreateModel(
            name='Parallax',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('unit', models.CharField(default=b'mas', max_length=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('unit', models.CharField(default=b'd', max_length=1, choices=[(b's', b'seconds'), (b'm', b'minutes'), (b'd', b'days'), (b'h', b'hours'), (b'w', b'weeks'), (b'y', b'years')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'', max_length=1000)),
                ('middle_name', models.CharField(default=b'', max_length=1000)),
                ('last_name', models.CharField(default=b'', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Radius',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('unit', models.CharField(default=b'sun', max_length=3, choices=[(b'sun', b'Sun'), (b'jup', b'Jupiter'), (b'nep', b'Neptune'), (b'eee', b'Earth')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('unit', models.CharField(default=b'K', max_length=1, choices=[(b'K', b'Kelvin'), (b'C', b'Celsius')])),
            ],
            options={
                'abstract': False,
            },
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
            name='Velocity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('unit', models.CharField(default=b'm/s', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dome',
            fields=[
                ('building_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='arcsecond.Building')),
            ],
            bases=('arcsecond.building',),
        ),
        migrations.CreateModel(
            name='Mirror',
            fields=[
                ('toolcomponent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='arcsecond.ToolComponent')),
                ('diameter', models.FloatField(null=True, blank=True)),
                ('thickness', models.FloatField(null=True, blank=True)),
                ('shape', models.CharField(max_length=1000, null=True, blank=True)),
                ('curvature', models.CharField(max_length=1000, null=True, blank=True)),
                ('coating', models.CharField(max_length=1000, null=True, blank=True)),
                ('central_obscuration', models.FloatField(null=True, blank=True)),
                ('material', models.CharField(max_length=1000, null=True, blank=True)),
                ('creation_date', models.DateField(null=True, blank=True)),
            ],
            bases=('arcsecond.toolcomponent',),
        ),
        migrations.CreateModel(
            name='ObservingTool',
            fields=[
                ('tool_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='arcsecond.Tool')),
            ],
            bases=('arcsecond.tool',),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='calculated_temperature',
            field=models.OneToOneField(related_name='calculated_temperature', null=True, blank=True, to='arcsecond.Temperature'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='coordinates',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.AstronomicalCoordinates'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='eccentricity',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.Eccentricity'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='geometric_albedo',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.Albedo'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='hottest_point_longitude',
            field=models.OneToOneField(related_name='hottest_point_longitude', null=True, blank=True, to='arcsecond.Angle'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='impact_parameter_b',
            field=models.OneToOneField(related_name='impact_parameter_b', null=True, blank=True, to='arcsecond.Angle'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='inclination',
            field=models.OneToOneField(related_name='inclination', null=True, blank=True, to='arcsecond.Angle'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='mass',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.Mass'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='measured_temperature',
            field=models.OneToOneField(related_name='measured_temperature', null=True, blank=True, to='arcsecond.Temperature'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='omega',
            field=models.OneToOneField(related_name='omega', null=True, blank=True, to='arcsecond.Angle'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='orbital_period',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.Period'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='parent_star',
            field=models.ForeignKey(related_name='planets', blank=True, to='arcsecond.AstronomicalObject', null=True),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='primary_transit',
            field=models.OneToOneField(related_name='primary_transit', null=True, blank=True, to='arcsecond.JulianDay'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='radius',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.Radius'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='secondary_transit',
            field=models.OneToOneField(related_name='secondary_transit', null=True, blank=True, to='arcsecond.JulianDay'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='semimajor_axis',
            field=models.OneToOneField(related_name='semimajor_axis', null=True, blank=True, to='arcsecond.EllipseAxis'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='surface_gravity',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.Gravity'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='time_periastron',
            field=models.OneToOneField(related_name='time_periastron', null=True, blank=True, to='arcsecond.JulianDay'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='time_vr0',
            field=models.OneToOneField(related_name='time_vr0', null=True, blank=True, to='arcsecond.JulianDay'),
        ),
        migrations.AddField(
            model_name='exoplanet',
            name='velocity_semiamplitude_K',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.Velocity'),
        ),
        migrations.AlterUniqueTogether(
            name='coordinates',
            unique_together=set([('longitude', 'latitude')]),
        ),
        migrations.AddField(
            model_name='building',
            name='coordinates',
            field=models.ManyToManyField(related_name='building', to='arcsecond.Coordinates', blank=True),
        ),
        migrations.AddField(
            model_name='bibliographicreference',
            name='authors',
            field=models.ManyToManyField(related_name='authors', to='arcsecond.Person'),
        ),
        migrations.AddField(
            model_name='astronomicalorganisation',
            name='headquarters',
            field=models.OneToOneField(related_name='astronomical_organisation', null=True, blank=True, to='arcsecond.ObservingSite'),
        ),
        migrations.AddField(
            model_name='astronomicalorganisation',
            name='observing_sites',
            field=models.ManyToManyField(related_name='astronomical_organisations', to='arcsecond.ObservingSite'),
        ),
        migrations.AddField(
            model_name='astronomicalobject',
            name='mass',
            field=models.OneToOneField(null=True, blank=True, to='arcsecond.Mass'),
        ),
        migrations.AddField(
            model_name='alias',
            name='astronomical_object',
            field=models.ForeignKey(related_name='aliases', blank=True, to='arcsecond.AstronomicalObject', null=True),
        ),
        migrations.AddField(
            model_name='alias',
            name='exoplanet',
            field=models.ForeignKey(related_name='aliases', blank=True, to='arcsecond.Exoplanet', null=True),
        ),
        migrations.CreateModel(
            name='Telescope',
            fields=[
                ('observingtool_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='arcsecond.ObservingTool')),
                ('wavelength_domains', multiselectfield.db.fields.MultiSelectField(max_length=51, choices=[(b'hga', b'Hard gamma-rays'), (b'wga', b'Weak gamma-rays'), (b'hxr', b'Hard x-rays'), (b'wxr', b'Weak x-rays'), (b'fuv', b'Far ultraviolet'), (b'nuv', b'Near ultraviolet'), (b'opt', b'Optical'), (b'nir', b'Near infrared'), (b'mir', b'Mid-infrared'), (b'fir', b'Far infrared'), (b'smm', b'Sub-milimetric'), (b'mmc', b'Milimetric'), (b'rad', b'Radio')])),
                ('mounting', models.CharField(max_length=3, choices=[(b'equ', b'Equatorial'), (b'cas', b'Cassegrain'), (b'aaz', b'Alt-Az')])),
                ('optical_design', models.CharField(blank=True, max_length=2, null=True, choices=[(b'rc', 'Ritchey-Chretien'), (b'sc', 'Schmidt')])),
                ('dome', models.OneToOneField(related_name='telescope', null=True, default=None, blank=True, to='arcsecond.Dome')),
            ],
            bases=('arcsecond.observingtool',),
        ),
        migrations.AddField(
            model_name='observingtool',
            name='coordinates',
            field=models.ManyToManyField(related_name='observing_tool', to='arcsecond.Coordinates'),
        ),
        migrations.AddField(
            model_name='mirror',
            name='telescope',
            field=models.ForeignKey(related_name='mirrors', default=None, blank=True, to='arcsecond.Telescope', null=True),
        ),
    ]
