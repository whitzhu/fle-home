# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gallery'
        db.create_table(u'ka_lite_gallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ka_lite', ['Gallery'])

        # Adding model 'Picture'
        db.create_table(u'ka_lite_picture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photos', to=orm['ka_lite.Gallery'])),
        ))
        db.send_create_signal(u'ka_lite', ['Picture'])

        # Adding model 'DeploymentStory'
        db.create_table(u'ka_lite_deploymentstory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('deployment_city', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('deployment_country', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('organization_name', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('organization_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('organization_city', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('organization_country', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('num_students', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('student_age_range', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
            ('num_kalite_servers', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('server_os', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
            ('hardware_setup', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('deployment_setting', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pedagogical_model', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('guest_blog_post', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('photo_gallery', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ka_lite.Gallery'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'ka_lite', ['DeploymentStory'])


    def backwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table(u'ka_lite_gallery')

        # Deleting model 'Picture'
        db.delete_table(u'ka_lite_picture')

        # Deleting model 'DeploymentStory'
        db.delete_table(u'ka_lite_deploymentstory')


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
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'num_kalite_servers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_students': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'organization_city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'organization_country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'organization_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'organization_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'pedagogical_model': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'photo_gallery': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ka_lite.Gallery']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'server_os': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'student_age_range': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ka_lite.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ka_lite.picture': {
            'Meta': {'object_name': 'Picture'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': u"orm['ka_lite.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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