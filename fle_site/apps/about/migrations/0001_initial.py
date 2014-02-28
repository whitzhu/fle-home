# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AboutSection'
        db.create_table('about_aboutsection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('body', self.gf('markupfield.fields.MarkupField')(rendered_field=True)),
            ('body_markup_type', self.gf('django.db.models.fields.CharField')(default=None, max_length=30)),
            ('_body_rendered', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('about', ['AboutSection'])


    def backwards(self, orm):
        # Deleting model 'AboutSection'
        db.delete_table('about_aboutsection')


    models = {
        'about.aboutsection': {
            'Meta': {'object_name': 'AboutSection'},
            '_body_rendered': ('django.db.models.fields.TextField', [], {}),
            'body': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'body_markup_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['about']