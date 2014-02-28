# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PressArticle'
        db.create_table('about_pressarticle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('publish_date', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('markupfield.fields.MarkupField')(rendered_field=True)),
            ('description_markup_type', self.gf('django.db.models.fields.CharField')(default=None, max_length=30)),
            ('_description_rendered', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('about', ['PressArticle'])


    def backwards(self, orm):
        # Deleting model 'PressArticle'
        db.delete_table('about_pressarticle')


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
        'about.pressarticle': {
            'Meta': {'object_name': 'PressArticle'},
            '_description_rendered': ('django.db.models.fields.TextField', [], {}),
            'description': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'description_markup_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'about.teammember': {
            'Meta': {'object_name': 'TeamMember', '_ormbases': ['about.Person']},
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['about.Person']", 'unique': 'True', 'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['about']