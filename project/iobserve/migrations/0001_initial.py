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
            ('altitude', self.gf('django.db.models.fields.FloatField')(default=-9999999999999)),
            ('east_positive', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('iobserve', ['TerrestrialCoordinates'])

        # Adding unique constraint on 'TerrestrialCoordinates', fields ['longitude', 'latitude']
        db.create_unique(u'iobserve_terrestrialcoordinates', ['longitude', 'latitude'])

        # Adding model 'Site'
        db.create_table(u'iobserve_site', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('coordinates', self.gf('django.db.models.fields.related.OneToOneField')(related_name='iobserve_site_related', unique=True, to=orm['iobserve.TerrestrialCoordinates'])),
            ('continent', self.gf('django.db.models.fields.CharField')(default='(Undefined)', max_length=100)),
            ('long_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('displayed_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('address_line_1', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('address_line_2', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('wikipedia_article', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('iobserve', ['Site'])

        # Adding model 'ObservingSite'
        db.create_table(u'iobserve_observingsite', (
            (u'site_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['iobserve.Site'], unique=True, primary_key=True)),
            ('IAUCode', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('iobserve', ['ObservingSite'])

        # Adding model 'ObservingPoint'
        db.create_table(u'iobserve_observingpoint', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('coordinates', self.gf('django.db.models.fields.related.OneToOneField')(related_name='iobserve_observingpoint_related', unique=True, to=orm['iobserve.TerrestrialCoordinates'])),
        ))
        db.send_create_signal('iobserve', ['ObservingPoint'])

        # Adding model 'AstronomicalOrganisation'
        db.create_table(u'iobserve_astronomicalorganisation', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('headquarters', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='astronomical_organisation', unique=True, null=True, to=orm['iobserve.Site'])),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('wikipedia_article', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
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

        # Deleting model 'Site'
        db.delete_table(u'iobserve_site')

        # Deleting model 'ObservingSite'
        db.delete_table(u'iobserve_observingsite')

        # Deleting model 'ObservingPoint'
        db.delete_table(u'iobserve_observingpoint')

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
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'headquarters': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'astronomical_organisation'", 'unique': 'True', 'null': 'True', 'to': "orm['iobserve.Site']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'observing_sites': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'astronomical_organisations'", 'symmetrical': 'False', 'to': "orm['iobserve.ObservingSite']"}),
            'organisation_type': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '100'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'wikipedia_article': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'iobserve.bibliographicreference': {
            'Meta': {'object_name': 'BibliographicReference'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'iobserve.observingpoint': {
            'Meta': {'object_name': 'ObservingPoint'},
            'coordinates': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'iobserve_observingpoint_related'", 'unique': 'True', 'to': "orm['iobserve.TerrestrialCoordinates']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'})
        },
        'iobserve.observingsite': {
            'IAUCode': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'ObservingSite', '_ormbases': ['iobserve.Site']},
            u'site_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['iobserve.Site']", 'unique': 'True', 'primary_key': 'True'})
        },
        'iobserve.person': {
            'Meta': {'object_name': 'Person'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'iobserve.site': {
            'Meta': {'object_name': 'Site'},
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'continent': ('django.db.models.fields.CharField', [], {'default': "'(Undefined)'", 'max_length': '100'}),
            'coordinates': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'iobserve_site_related'", 'unique': 'True', 'to': "orm['iobserve.TerrestrialCoordinates']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'displayed_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'wikipedia_article': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'iobserve.terrestrialcoordinates': {
            'Meta': {'ordering': "['longitude', 'latitude']", 'unique_together': "(('longitude', 'latitude'),)", 'object_name': 'TerrestrialCoordinates'},
            'altitude': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'}),
            'east_positive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'})
        }
    }

    complete_apps = ['iobserve']