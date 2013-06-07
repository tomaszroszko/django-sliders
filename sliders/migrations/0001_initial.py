# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slider'
        db.create_table(u'sliders_slider', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug_name', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'sliders', ['Slider'])

        # Adding model 'SliderPhoto'
        db.create_table(u'sliders_sliderphoto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sliders.Slider'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('active_from', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('active_to', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'sliders', ['SliderPhoto'])


    def backwards(self, orm):
        # Deleting model 'Slider'
        db.delete_table(u'sliders_slider')

        # Deleting model 'SliderPhoto'
        db.delete_table(u'sliders_sliderphoto')


    models = {
        u'sliders.slider': {
            'Meta': {'object_name': 'Slider'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug_name': ('django.db.models.fields.SlugField', [], {'max_length': '255'})
        },
        u'sliders.sliderphoto': {
            'Meta': {'ordering': "('order',)", 'object_name': 'SliderPhoto'},
            'active_from': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'active_to': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sliders.Slider']"})
        }
    }

    complete_apps = ['sliders']