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

        # Adding model 'TeamMember'
        db.create_table('about_teammember', (
            ('person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['about.Person'], unique=True, primary_key=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('about', ['TeamMember'])

        # Adding model 'BoardMember'
        db.create_table('about_boardmember', (
            ('person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['about.Person'], unique=True, primary_key=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('about', ['BoardMember'])

        # Adding model 'PressLogo'
        db.create_table('about_presslogo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('about', ['PressLogo'])

        # Adding model 'PressArticle'
        db.create_table('about_pressarticle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('publish_date', self.gf('django.db.models.fields.DateField')()),
            ('logo', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['about.PressLogo'], blank=True)),
        ))
        db.send_create_signal('about', ['PressArticle'])

        # Adding model 'Internship'
        db.create_table('about_internship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('description', self.gf('markupfield.fields.MarkupField')(rendered_field=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('description_markup_type', self.gf('django.db.models.fields.CharField')(default='html', max_length=30)),
            ('_description_rendered', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('about', ['Internship'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('about_person')

        # Deleting model 'TeamMember'
        db.delete_table('about_teammember')

        # Deleting model 'BoardMember'
        db.delete_table('about_boardmember')

        # Deleting model 'PressLogo'
        db.delete_table('about_presslogo')

        # Deleting model 'PressArticle'
        db.delete_table('about_pressarticle')

        # Deleting model 'Internship'
        db.delete_table('about_internship')


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
        'about.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
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
        'about.teammember': {
            'Meta': {'object_name': 'TeamMember', '_ormbases': ['about.Person']},
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['about.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['about']