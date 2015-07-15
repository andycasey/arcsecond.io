# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
from django.conf import settings
import django.core.validators


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
            name='AstronomicalAge',
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
            name='AstronomicalAngularDistance',
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
            name='AstronomicalColor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('firstMagnitudeName', models.CharField(max_length=2)),
                ('secondMagnitudeName', models.CharField(max_length=2)),
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
            name='AstronomicalDistance',
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
            name='AstronomicalEccentricity',
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
            name='AstronomicalEffectiveTemperature',
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
            name='AstronomicalFlux',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=-9999999999999, null=True)),
                ('error', models.FloatField(default=-9999999999999, null=True)),
                ('error_up', models.FloatField(default=-9999999999999, null=True)),
                ('error_down', models.FloatField(default=-9999999999999, null=True)),
                ('bibcode', models.CharField(default=b'', max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[0-9]{4}[A-Za-z].{12}[0-9][A-Z]$', message=b'Invalid bibcode', code=b'nomatch')])),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AstronomicalInclination',
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
            name='AstronomicalMass',
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
            name='AstronomicalMetallicity',
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
            name='AstronomicalObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('coordinates', models.OneToOneField(null=True, to='iobserve.AstronomicalCoordinates')),
                ('mass', models.OneToOneField(null=True, to='iobserve.AstronomicalMass')),
            ],
        ),
        migrations.CreateModel(
            name='AstronomicalOrbitalPeriod',
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
            name='AstronomicalParallax',
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
            name='AstronomicalRadius',
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
            name='AstronomicalSemiMajorAxis',
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
            name='Exoplanet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('mass', models.FloatField(default=-9999999999999)),
                ('coordinates', models.OneToOneField(null=True, to='iobserve.AstronomicalCoordinates')),
                ('parent_star', models.ForeignKey(related_name='planets', blank=True, to='iobserve.AstronomicalObject', null=True)),
            ],
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
                ('first_name', models.CharField(default=b'', max_length=1000)),
                ('middle_name', models.CharField(default=b'', max_length=1000)),
                ('last_name', models.CharField(default=b'', max_length=1000)),
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
            model_name='bibliographicreference',
            name='authors',
            field=models.ManyToManyField(related_name='authors', to='iobserve.Person'),
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
