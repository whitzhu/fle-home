# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrganizationType'
        db.create_table('about_organizationtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('about', ['OrganizationType'])

        # Adding model 'SupportingOrganization'
        db.create_table('about_supportingorganization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, blank=True)),
            ('description', self.gf('markupfield.fields.MarkupField')(rendered_field=True)),
            ('organization_type', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['about.OrganizationType'], blank=True)),
            ('description_markup_type', self.gf('django.db.models.fields.CharField')(default='html', max_length=30)),
            ('_description_rendered', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('about', ['SupportingOrganization'])


    def backwards(self, orm):
        # Deleting model 'OrganizationType'
        db.delete_table('about_organizationtype')

        # Deleting model 'SupportingOrganization'
        db.delete_table('about_supportingorganization')


    models = {
        'about.boardmember': {
            'Meta': {'object_name': 'BoardMember', '_ormbases': ['about.Person']},
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['about.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'about.internship': {
            'Meta': {'object_name': 'Internship'},
            '_description_rendered': ('django.db.models.fields.TextField', [], {}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'description_markup_type': ('django.db.models.fields.CharField', [], {'default': "'html'", 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'about.organizationtype': {
            'Meta': {'object_name': 'OrganizationType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'about.person': {
            'Meta': {'object_name': 'Person'},
            '_bio_rendered': ('django.db.models.fields.TextField', [], {}),
            'bio': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'bio_markup_type': ('django.db.models.fields.CharField', [], {'default': "'html'", 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'about.pressarticle': {
            'Meta': {'object_name': 'PressArticle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['about.PressLogo']", 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'about.presslogo': {
            'Meta': {'object_name': 'PressLogo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'about.supportingorganization': {
            'Meta': {'object_name': 'SupportingOrganization'},
            '_description_rendered': ('django.db.models.fields.TextField', [], {}),
            'description': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'description_markup_type': ('django.db.models.fields.CharField', [], {'default': "'html'", 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organization_type': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['about.OrganizationType']", 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'about.teammember': {
            'Meta': {'object_name': 'TeamMember', '_ormbases': ['about.Person']},
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['about.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['about']