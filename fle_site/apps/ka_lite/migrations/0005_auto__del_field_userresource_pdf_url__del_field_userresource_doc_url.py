# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UserResource.pdf_url'
        db.delete_column(u'ka_lite_userresource', 'pdf_url')

        # Deleting field 'UserResource.doc_url'
        db.delete_column(u'ka_lite_userresource', 'doc_url')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'UserResource.pdf_url'
        raise RuntimeError("Cannot reverse this migration. 'UserResource.pdf_url' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'UserResource.pdf_url'
        db.add_column(u'ka_lite_userresource', 'pdf_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'UserResource.doc_url'
        raise RuntimeError("Cannot reverse this migration. 'UserResource.doc_url' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'UserResource.doc_url'
        db.add_column(u'ka_lite_userresource', 'doc_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200),
                      keep_default=False)


    models = {
        u'ka_lite.userresource': {
            'Meta': {'object_name': 'UserResource'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'doc_id': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['ka_lite']