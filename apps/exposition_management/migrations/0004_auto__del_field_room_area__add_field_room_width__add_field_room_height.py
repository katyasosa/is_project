# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Room.area'
        db.delete_column(u'exposition_management_room', 'area')

        # Adding field 'Room.width'
        db.add_column(u'exposition_management_room', 'width',
                      self.gf('django.db.models.fields.IntegerField')(default=10),
                      keep_default=False)

        # Adding field 'Room.height'
        db.add_column(u'exposition_management_room', 'height',
                      self.gf('django.db.models.fields.IntegerField')(default=10),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Room.area'
        db.add_column(u'exposition_management_room', 'area',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Room.width'
        db.delete_column(u'exposition_management_room', 'width')

        # Deleting field 'Room.height'
        db.delete_column(u'exposition_management_room', 'height')


    models = {
        u'exposition_management.exposition': {
            'Meta': {'object_name': 'Exposition'},
            'closing_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'opening_date': ('django.db.models.fields.DateField', [], {}),
            'plants': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['exposition_management.Plant']", 'through': u"orm['exposition_management.PlantPosition']", 'symmetrical': 'False'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exposition_management.Room']"}),
            'stage': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'exposition_management.plant': {
            'Meta': {'object_name': 'Plant'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exposition_management.PlantSpecies']"})
        },
        u'exposition_management.plantposition': {
            'Meta': {'object_name': 'PlantPosition'},
            'exposition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exposition_management.Exposition']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exposition_management.Plant']"}),
            'position_x': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position_y': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'exposition_management.plantspecies': {
            'Meta': {'object_name': 'PlantSpecies'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django_thumbs.db.models.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'exposition_management.room': {
            'Meta': {'object_name': 'Room'},
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django_thumbs.db.models.ImageWithThumbsField', [], {'max_length': '100'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['exposition_management']