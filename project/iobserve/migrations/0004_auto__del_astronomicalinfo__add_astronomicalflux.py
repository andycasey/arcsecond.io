# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'AstronomicalInfo'
        db.delete_table(u'iobserve_astronomicalinfo')

        # Adding model 'AstronomicalFlux'
        db.create_table(u'iobserve_astronomicalflux', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('value', self.gf('django.db.models.fields.FloatField')(default=-9999999999999)),
            ('error_value', self.gf('django.db.models.fields.FloatField')(default=-9999999999999)),
            ('bibcode', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('astronomical_object', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fluxes', null=True, to=orm['iobserve.AstronomicalObject'])),
        ))
        db.send_create_signal('iobserve', ['AstronomicalFlux'])


    def backwards(self, orm):
        # Adding model 'AstronomicalInfo'
        db.create_table(u'iobserve_astronomicalinfo', (
            ('error_value', self.gf('django.db.models.fields.FloatField')(default=-9999999999999)),
            ('string_value', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('string_unit', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.FloatField')(default=-9999999999999)),
            ('bibcode', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('unit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('iobserve', ['AstronomicalInfo'])

        # Deleting model 'AstronomicalFlux'
        db.delete_table(u'iobserve_astronomicalflux')


    models = {
        'iobserve.alias': {
            'Meta': {'object_name': 'Alias'},
            'astronomical_object': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'aliases'", 'null': 'True', 'to': "orm['iobserve.AstronomicalObject']"}),
            'catalogue_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'iobserve.astronomicalcoordinates': {
            'Meta': {'object_name': 'AstronomicalCoordinates'},
            'declination': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'}),
            'declination_units': ('django.db.models.fields.CharField', [], {'default': "'degrees'", 'max_length': '100'}),
            'epoch': ('django.db.models.fields.FloatField', [], {'default': '2000'}),
            'equinox': ('django.db.models.fields.FloatField', [], {'default': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'right_ascension': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'}),
            'right_ascension_units': ('django.db.models.fields.CharField', [], {'default': "'degrees'", 'max_length': '100'})
        },
        'iobserve.astronomicalflux': {
            'Meta': {'object_name': 'AstronomicalFlux'},
            'astronomical_object': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fluxes'", 'null': 'True', 'to': "orm['iobserve.AstronomicalObject']"}),
            'bibcode': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'error_value': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'value': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'})
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
        'iobserve.objecttype': {
            'Meta': {'object_name': 'ObjectType'},
            'astronomical_object': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'object_types'", 'null': 'True', 'to': "orm['iobserve.AstronomicalObject']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '500'})
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