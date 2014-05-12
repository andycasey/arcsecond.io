# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'iobserve_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal('iobserve', ['Person'])

        # Adding model 'BibliographicReference'
        db.create_table(u'iobserve_bibliographicreference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('iobserve', ['BibliographicReference'])

        # Adding model 'TerrestrialCoordinates'
        db.create_table(u'iobserve_terrestrialcoordinates', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(default=-9999999999999)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(default=-9999999999999)),
            ('east_positive', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('altitude', self.gf('django.db.models.fields.FloatField')(default=-9999999999999)),
        ))
        db.send_create_signal('iobserve', ['TerrestrialCoordinates'])

        # Adding unique constraint on 'TerrestrialCoordinates', fields ['longitude', 'latitude']
        db.create_unique(u'iobserve_terrestrialcoordinates', ['longitude', 'latitude'])

        # Adding model 'TerrestrialObject'
        db.create_table(u'iobserve_terrestrialobject', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('long_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('continent', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('iobserve', ['TerrestrialObject'])

        # Adding model 'ObservingTool'
        db.create_table(u'iobserve_observingtool', (
            (u'terrestrialobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['iobserve.TerrestrialObject'], unique=True, primary_key=True)),
            ('tool_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sites', to=orm['iobserve.ObservingSite'])),
        ))
        db.send_create_signal('iobserve', ['ObservingTool'])

        # Adding model 'Site'
        db.create_table(u'iobserve_site', (
            (u'terrestrialobject_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['iobserve.TerrestrialObject'], unique=True, primary_key=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address_line_1', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address_line_2', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('zip_code', self.gf('django.db.models.fields.IntegerField')()),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('wikipedia_article', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('iobserve', ['Site'])

        # Adding model 'ObservingSite'
        db.create_table(u'iobserve_observingsite', (
            (u'site_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['iobserve.Site'], unique=True, primary_key=True)),
            ('IAUCode', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('iobserve', ['ObservingSite'])

        # Adding model 'AstronomicalOrganisation'
        db.create_table(u'iobserve_astronomicalorganisation', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('headquarters', self.gf('django.db.models.fields.related.OneToOneField')(related_name='astronomical_organisation', unique=True, to=orm['iobserve.Site'])),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('wikipedia_article', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('organisation_type', self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=100)),
        ))
        db.send_create_signal('iobserve', ['AstronomicalOrganisation'])

        # Adding M2M table for field observing_sites on 'AstronomicalOrganisation'
        m2m_table_name = db.shorten_name(u'iobserve_astronomicalorganisation_observing_sites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('astronomicalorganisation', models.ForeignKey(orm['iobserve.astronomicalorganisation'], null=False)),
            ('observingsite', models.ForeignKey(orm['iobserve.observingsite'], null=False))
        ))
        db.create_unique(m2m_table_name, ['astronomicalorganisation_id', 'observingsite_id'])

        # Adding model 'AstronomicalCoordinates'
        db.create_table(u'iobserve_astronomicalcoordinates', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('right_ascension', self.gf('django.db.models.fields.FloatField')(default=-9999999999999)),
            ('declination', self.gf('django.db.models.fields.FloatField')(default=-9999999999999)),
            ('epoch', self.gf('django.db.models.fields.FloatField')(default=2000)),
            ('equinox', self.gf('django.db.models.fields.FloatField')(default=2000)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
        ))
        db.send_create_signal('iobserve', ['AstronomicalCoordinates'])

        # Adding model 'Alias'
        db.create_table(u'iobserve_alias', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('astronomical_object', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='aliases', null=True, to=orm['iobserve.AstronomicalObject'])),
        ))
        db.send_create_signal('iobserve', ['Alias'])

        # Adding model 'AstronomicalObject'
        db.create_table(u'iobserve_astronomicalobject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('coordinates', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['iobserve.AstronomicalCoordinates'], unique=True, null=True)),
        ))
        db.send_create_signal('iobserve', ['AstronomicalObject'])


    def backwards(self, orm):
        # Removing unique constraint on 'TerrestrialCoordinates', fields ['longitude', 'latitude']
        db.delete_unique(u'iobserve_terrestrialcoordinates', ['longitude', 'latitude'])

        # Deleting model 'Person'
        db.delete_table(u'iobserve_person')

        # Deleting model 'BibliographicReference'
        db.delete_table(u'iobserve_bibliographicreference')

        # Deleting model 'TerrestrialCoordinates'
        db.delete_table(u'iobserve_terrestrialcoordinates')

        # Deleting model 'TerrestrialObject'
        db.delete_table(u'iobserve_terrestrialobject')

        # Deleting model 'ObservingTool'
        db.delete_table(u'iobserve_observingtool')

        # Deleting model 'Site'
        db.delete_table(u'iobserve_site')

        # Deleting model 'ObservingSite'
        db.delete_table(u'iobserve_observingsite')

        # Deleting model 'AstronomicalOrganisation'
        db.delete_table(u'iobserve_astronomicalorganisation')

        # Removing M2M table for field observing_sites on 'AstronomicalOrganisation'
        db.delete_table(db.shorten_name(u'iobserve_astronomicalorganisation_observing_sites'))

        # Deleting model 'AstronomicalCoordinates'
        db.delete_table(u'iobserve_astronomicalcoordinates')

        # Deleting model 'Alias'
        db.delete_table(u'iobserve_alias')

        # Deleting model 'AstronomicalObject'
        db.delete_table(u'iobserve_astronomicalobject')


    models = {
        'iobserve.alias': {
            'Meta': {'object_name': 'Alias'},
            'astronomical_object': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'aliases'", 'null': 'True', 'to': "orm['iobserve.AstronomicalObject']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'iobserve.astronomicalcoordinates': {
            'Meta': {'object_name': 'AstronomicalCoordinates'},
            'declination': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'}),
            'epoch': ('django.db.models.fields.FloatField', [], {'default': '2000'}),
            'equinox': ('django.db.models.fields.FloatField', [], {'default': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'right_ascension': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'})
        },
        'iobserve.astronomicalobject': {
            'Meta': {'object_name': 'AstronomicalObject'},
            'coordinates': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['iobserve.AstronomicalCoordinates']", 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'iobserve.astronomicalorganisation': {
            'Meta': {'object_name': 'AstronomicalOrganisation'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'headquarters': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'astronomical_organisation'", 'unique': 'True', 'to': "orm['iobserve.Site']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'observing_sites': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'astronomical_organisations'", 'symmetrical': 'False', 'to': "orm['iobserve.ObservingSite']"}),
            'organisation_type': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '100'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'wikipedia_article': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'iobserve.bibliographicreference': {
            'Meta': {'object_name': 'BibliographicReference'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'iobserve.observingsite': {
            'IAUCode': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'ObservingSite', '_ormbases': ['iobserve.Site']},
            u'site_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['iobserve.Site']", 'unique': 'True', 'primary_key': 'True'})
        },
        'iobserve.observingtool': {
            'Meta': {'object_name': 'ObservingTool', '_ormbases': ['iobserve.TerrestrialObject']},
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sites'", 'to': "orm['iobserve.ObservingSite']"}),
            u'terrestrialobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['iobserve.TerrestrialObject']", 'unique': 'True', 'primary_key': 'True'}),
            'tool_type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'iobserve.person': {
            'Meta': {'object_name': 'Person'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'iobserve.site': {
            'Meta': {'object_name': 'Site', '_ormbases': ['iobserve.TerrestrialObject']},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'terrestrialobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['iobserve.TerrestrialObject']", 'unique': 'True', 'primary_key': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'wikipedia_article': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {})
        },
        'iobserve.terrestrialcoordinates': {
            'Meta': {'unique_together': "(('longitude', 'latitude'),)", 'object_name': 'TerrestrialCoordinates'},
            'altitude': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'}),
            'east_positive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'})
        },
        'iobserve.terrestrialobject': {
            'Meta': {'object_name': 'TerrestrialObject'},
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'})
        }
    }

    complete_apps = ['iobserve']