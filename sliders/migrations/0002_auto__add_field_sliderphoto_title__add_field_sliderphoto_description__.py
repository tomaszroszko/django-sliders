# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SliderPhoto.title'
        db.add_column(u'sliders_sliderphoto', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SliderPhoto.description'
        db.add_column(u'sliders_sliderphoto', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SliderPhoto.links_to'
        db.add_column(u'sliders_sliderphoto', 'links_to',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


        # Changing field 'SliderPhoto.image'
        db.alter_column(u'sliders_sliderphoto', 'image', self.gf('filebrowser.fields.FileBrowseField')(max_length=255))

    def backwards(self, orm):
        # Deleting field 'SliderPhoto.title'
        db.delete_column(u'sliders_sliderphoto', 'title')

        # Deleting field 'SliderPhoto.description'
        db.delete_column(u'sliders_sliderphoto', 'description')

        # Deleting field 'SliderPhoto.links_to'
        db.delete_column(u'sliders_sliderphoto', 'links_to')


        # Changing field 'SliderPhoto.image'
        db.alter_column(u'sliders_sliderphoto', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

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
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'links_to': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sliders.Slider']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sliders']