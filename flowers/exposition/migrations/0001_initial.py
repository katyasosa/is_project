# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Room'
        db.create_table(u'exposition_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'exposition', ['Room'])

        # Adding model 'PlantSpecies'
        db.create_table(u'exposition_plantspecies', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'exposition', ['PlantSpecies'])

        # Adding model 'Plant'
        db.create_table(u'exposition_plant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('species', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exposition.PlantSpecies'])),
        ))
        db.send_create_signal(u'exposition', ['Plant'])

        # Adding model 'Exposition'
        db.create_table(u'exposition_exposition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exposition.Room'])),
            ('stage', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('begin', self.gf('django.db.models.fields.DateField')()),
            ('end', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'exposition', ['Exposition'])

        # Adding M2M table for field plants on 'Exposition'
        db.create_table(u'exposition_exposition_plants', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exposition', models.ForeignKey(orm[u'exposition.exposition'], null=False)),
            ('plant', models.ForeignKey(orm[u'exposition.plant'], null=False))
        ))
        db.create_unique(u'exposition_exposition_plants', ['exposition_id', 'plant_id'])


    def backwards(self, orm):
        # Deleting model 'Room'
        db.delete_table(u'exposition_room')

        # Deleting model 'PlantSpecies'
        db.delete_table(u'exposition_plantspecies')

        # Deleting model 'Plant'
        db.delete_table(u'exposition_plant')

        # Deleting model 'Exposition'
        db.delete_table(u'exposition_exposition')

        # Removing M2M table for field plants on 'Exposition'
        db.delete_table('exposition_exposition_plants')


    models = {
        u'exposition.exposition': {
            'Meta': {'object_name': 'Exposition'},
            'begin': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'plants': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['exposition.Plant']", 'symmetrical': 'False'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exposition.Room']"}),
            'stage': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'exposition.plant': {
            'Meta': {'object_name': 'Plant'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exposition.PlantSpecies']"})
        },
        u'exposition.plantspecies': {
            'Meta': {'object_name': 'PlantSpecies'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'exposition.room': {
            'Meta': {'object_name': 'Room'},
            'area': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['exposition']