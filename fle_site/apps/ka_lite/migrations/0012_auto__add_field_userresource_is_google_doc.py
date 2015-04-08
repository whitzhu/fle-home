# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserResource.is_google_doc'
        db.add_column(u'ka_lite_userresource', 'is_google_doc',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'UserResource.external_url'
        db.add_column(u'ka_lite_userresource', 'external_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserResource.is_google_doc'
        db.delete_column(u'ka_lite_userresource', 'is_google_doc')

        # Deleting field 'UserResource.external_url'
        db.delete_column(u'ka_lite_userresource', 'external_url')


    models = {
        u'ka_lite.deploymentstory': {
            'Meta': {'object_name': 'DeploymentStory'},
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'deployment_city': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'deployment_country': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'deployment_setting': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'guest_blog_post': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'hardware_setup': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'num_kalite_servers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_students': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'organization_city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'organization_country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'organization_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'organization_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'pedagogical_model': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'photo_gallery': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ka_lite.Gallery']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'server_os': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_date_raw': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'student_age_range': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'testimonials': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'ka_lite.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ka_lite.picture': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Picture'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': u"orm['ka_lite.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'sort_order': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ka_lite.userresource': {
            'Meta': {'object_name': 'UserResource'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'doc_id': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'doc_type': ('django.db.models.fields.CharField', [], {'default': "'document'", 'max_length': '80'}),
            'external_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_google_doc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['ka_lite']