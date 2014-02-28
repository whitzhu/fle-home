# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('about_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('about', ['Person'])

        # Adding model 'BoardMember'
        db.create_table('about_boardmember', (
            ('person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['about.Person'], unique=True, primary_key=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('about', ['BoardMember'])

        # Adding model 'TeamMember'
        db.create_table('about_teammember', (
            ('person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['about.Person'], unique=True, primary_key=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('about', ['TeamMember'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('about_person')

        # Deleting model 'BoardMember'
        db.delete_table('about_boardmember')

        # Deleting model 'TeamMember'
        db.delete_table('about_teammember')


    models = {
        'about.aboutsection': {
            'Meta': {'object_name': 'AboutSection'},
            '_body_rendered': ('django.db.models.fields.TextField', [], {}),
            'body': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'body_markup_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'about.boardmember': {
            'Meta': {'object_name': 'BoardMember', '_ormbases': ['about.Person']},
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['about.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'about.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'about.teammember': {
            'Meta': {'object_name': 'TeamMember', '_ormbases': ['about.Person']},
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['about.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['about']