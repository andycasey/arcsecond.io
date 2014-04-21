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
        db.send_create_signal(u'iobserve', ['Person'])

        # Adding field 'AstronomicalCoordinates.source'
        db.add_column(u'iobserve_astronomicalcoordinates', 'source',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1000, blank=True),
                      keep_default=False)

        # Adding field 'BibliographicReference.year'
        db.add_column(u'iobserve_bibliographicreference', 'year',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding M2M table for field aliases on 'AstronomicalObject'
        m2m_table_name = db.shorten_name(u'iobserve_astronomicalobject_aliases')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('astronomicalobject', models.ForeignKey(orm[u'iobserve.astronomicalobject'], null=False)),
            ('alias', models.ForeignKey(orm[u'iobserve.alias'], null=False))
        ))
        db.create_unique(m2m_table_name, ['astronomicalobject_id', 'alias_id'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'iobserve_person')

        # Deleting field 'AstronomicalCoordinates.source'
        db.delete_column(u'iobserve_astronomicalcoordinates', 'source')

        # Deleting field 'BibliographicReference.year'
        db.delete_column(u'iobserve_bibliographicreference', 'year')

        # Removing M2M table for field aliases on 'AstronomicalObject'
        db.delete_table(db.shorten_name(u'iobserve_astronomicalobject_aliases'))


    models = {
        u'iobserve.alias': {
            'Meta': {'object_name': 'Alias'},
            'astronomical_object': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'alias'", 'to': u"orm['iobserve.AstronomicalObject']"}),
            'catalogue_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'iobserve.astronomicalcoordinates': {
            'Meta': {'object_name': 'AstronomicalCoordinates'},
            'declination': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'}),
            'epoch': ('django.db.models.fields.FloatField', [], {'default': '2000'}),
            'equinox': ('django.db.models.fields.FloatField', [], {'default': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'right_ascension': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'})
        },
        u'iobserve.astronomicalobject': {
            'Meta': {'object_name': 'AstronomicalObject'},
            'aliases': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'aliases'", 'blank': 'True', 'to': u"orm['iobserve.Alias']"}),
            'coordinates': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['iobserve.AstronomicalCoordinates']", 'unique': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'iobserve.astronomicalorganisation': {
            'Meta': {'object_name': 'AstronomicalOrganisation'},
            'headquarters': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'headquarters'", 'unique': 'True', 'to': u"orm['iobserve.Site']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observing_sites': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'observing_sites'", 'symmetrical': 'False', 'to': u"orm['iobserve.ObservingSite']"}),
            'secondary_headquarters': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'secondary_headquarters'", 'unique': 'True', 'to': u"orm['iobserve.Site']"})
        },
        u'iobserve.bibliographicreference': {
            'Meta': {'object_name': 'BibliographicReference'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'iobserve.observingsite': {
            'Meta': {'object_name': 'ObservingSite', '_ormbases': [u'iobserve.Site']},
            u'site_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['iobserve.Site']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'iobserve.observingtool': {
            'Meta': {'object_name': 'ObservingTool', '_ormbases': [u'iobserve.TerrestrialObject']},
            u'terrestrialobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['iobserve.TerrestrialObject']", 'unique': 'True', 'primary_key': 'True'}),
            'tool_type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'iobserve.person': {
            'Meta': {'object_name': 'Person'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'iobserve.site': {
            'Meta': {'object_name': 'Site', '_ormbases': [u'iobserve.TerrestrialObject']},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'site_type': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '100'}),
            u'terrestrialobject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['iobserve.TerrestrialObject']", 'unique': 'True', 'primary_key': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {})
        },
        u'iobserve.terrestrialcoordinates': {
            'Meta': {'object_name': 'TerrestrialCoordinates'},
            'altitude': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'}),
            'east_positive': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': '-9999999999999'})
        },
        u'iobserve.terrestrialobject': {
            'Meta': {'object_name': 'TerrestrialObject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['iobserve']