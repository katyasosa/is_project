# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Room'
        db.create_table(u'exposition_management_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.IntegerField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'exposition_management', ['Room'])

        # Adding model 'PlantSpecies'
        db.create_table(u'exposition_management_plantspecies', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'exposition_management', ['PlantSpecies'])

        # Adding model 'Plant'
        db.create_table(u'exposition_management_plant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('species', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exposition_management.PlantSpecies'])),
        ))
        db.send_create_signal(u'exposition_management', ['Plant'])

        # Adding model 'Exposition'
        db.create_table(u'exposition_management_exposition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exposition_management.Room'])),
            ('stage', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('begin', self.gf('django.db.models.fields.DateField')()),
            ('end', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'exposition_management', ['Exposition'])

        # Adding model 'PlantPosition'
        db.create_table(u'exposition_management_plantposition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exposition_management.Plant'])),
            ('exposition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exposition_management.Exposition'])),
            ('position_x', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('position_y', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'exposition_management', ['PlantPosition'])


    def backwards(self, orm):
        # Deleting model 'Room'
        db.delete_table(u'exposition_management_room')

        # Deleting model 'PlantSpecies'
        db.delete_table(u'exposition_management_plantspecies')

        # Deleting model 'Plant'
        db.delete_table(u'exposition_management_plant')

        # Deleting model 'Exposition'
        db.delete_table(u'exposition_management_exposition')

        # Deleting model 'PlantPosition'
        db.delete_table(u'exposition_management_plantposition')


    models = {
        u'exposition_management.exposition': {
            'Meta': {'object_name': 'Exposition'},
            'begin': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'exposition_management.room': {
            'Meta': {'object_name': 'Room'},
            'area': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['exposition_management']