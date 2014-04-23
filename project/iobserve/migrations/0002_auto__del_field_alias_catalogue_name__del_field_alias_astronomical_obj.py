# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Alias.catalogue_name'
        db.delete_column(u'iobserve_alias', 'catalogue_name')

        # Deleting field 'Alias.astronomical_object'
        db.delete_column(u'iobserve_alias', 'astronomical_object_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Alias.catalogue_name'
        raise RuntimeError("Cannot reverse this migration. 'Alias.catalogue_name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Alias.catalogue_name'
        db.add_column(u'iobserve_alias', 'catalogue_name',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Alias.astronomical_object'
        raise RuntimeError("Cannot reverse this migration. 'Alias.astronomical_object' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Alias.astronomical_object'
        db.add_column(u'iobserve_alias', 'astronomical_object',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='alias', to=orm['iobserve.AstronomicalObject']),
                      keep_default=False)


    models = {
        'iobserve.alias': {
            'Meta': {'object_name': 'Alias'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'aliases': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'aliases'", 'blank': 'True', 'to': "orm['iobserve.Alias']"}),
            'coordinates': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['iobserve.AstronomicalCoordinates']", 'unique': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'iobserve.astronomicalorganisation': {
            'Meta': {'object_name': 'AstronomicalOrganisation'},
            'headquarters': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'headquarters'", 'unique': 'True', 'to': "orm['iobserve.Site']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observing_sites': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'observing_sites'", 'symmetrical': 'False', 'to': "orm['iobserve.ObservingSite']"}),
            'secondary_headquarters': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'secondary_headquarters'", 'unique': 'True', 'to': "orm['iobserve.Site']"})
        },
        'iobserve.bibliographicreference': {
            'Meta': {'object_name': 'BibliographicReference'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'iobserve.observingsite': {
            'Meta': {'object_name': 'ObservingSite', '_ormbases': ['iobserve.Site']},
            u'site_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['iobserve.Site']", 'unique': 'True', 'primary_key': 'True'})
        },
        'iobserve.observingtool': {
            'Meta': {'object_name': 'ObservingTool', '_ormbases': ['iobserve.TerrestrialObject']},
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
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'site_type': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '100'}),
            u'terrestrialobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['iobserve.TerrestrialObject']", 'unique': 'True', 'primary_key': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {})
        },
        'iobserve.terrestrialcoordinates': {
            'Meta': {'object_name': 'TerrestrialCoordinates'},
            'altitude': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'}),
            'east_positive': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'})
        },
        'iobserve.terrestrialobject': {
            'Meta': {'object_name': 'TerrestrialObject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['iobserve']