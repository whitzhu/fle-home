# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UserResource.last_updated'
        db.delete_column(u'ka_lite_userresource', 'last_updated')

        # Deleting field 'UserResource.publish_date'
        db.delete_column(u'ka_lite_userresource', 'publish_date')

        # Adding field 'UserResource.doc_id'
        db.add_column(u'ka_lite_userresource', 'doc_id',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=80),
                      keep_default=False)

        # Adding field 'UserResource.filename'
        db.add_column(u'ka_lite_userresource', 'filename',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'UserResource.last_updated'
        db.add_column(u'ka_lite_userresource', 'last_updated',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 7, 2, 0, 0)),
                      keep_default=False)

        # Adding field 'UserResource.publish_date'
        db.add_column(u'ka_lite_userresource', 'publish_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 7, 2, 0, 0)),
                      keep_default=False)

        # Deleting field 'UserResource.doc_id'
        db.delete_column(u'ka_lite_userresource', 'doc_id')

        # Deleting field 'UserResource.filename'
        db.delete_column(u'ka_lite_userresource', 'filename')


    models = {
        u'ka_lite.userresource': {
            'Meta': {'object_name': 'UserResource'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'doc_id': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'doc_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pdf_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['ka_lite']