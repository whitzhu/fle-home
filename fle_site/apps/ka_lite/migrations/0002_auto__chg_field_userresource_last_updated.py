# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'UserResource.last_updated'
        db.alter_column(u'ka_lite_userresource', 'last_updated', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'UserResource.last_updated'
        db.alter_column(u'ka_lite_userresource', 'last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    models = {
        u'ka_lite.userresource': {
            'Meta': {'object_name': 'UserResource'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'doc_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'pdf_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['ka_lite']