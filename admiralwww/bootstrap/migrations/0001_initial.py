# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Params'
        db.create_table('bootstrap_params', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=50, db_index=True)),
            ('value', self.gf('django.db.models.fields.TextField')()),
            ('hint', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('bootstrap', ['Params'])


    def backwards(self, orm):
        # Deleting model 'Params'
        db.delete_table('bootstrap_params')


    models = {
        'bootstrap.params': {
            'Meta': {'object_name': 'Params'},
            'hint': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['bootstrap']