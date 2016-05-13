# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Nds.value'
        db.add_column('bootstrap_nds', 'value',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Nds.value'
        db.delete_column('bootstrap_nds', 'value')


    models = {
        'bootstrap.measure': {
            'Meta': {'object_name': 'Measure'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'bootstrap.nds': {
            'Meta': {'object_name': 'Nds'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'bootstrap.params': {
            'Meta': {'object_name': 'Params'},
            'hint': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        'bootstrap.portrate': {
            'Meta': {'object_name': 'PortRate'},
            'dangerous_20': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'dangerous_40': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'not_dangerous_20': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'not_dangerous_40': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'port_servicie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bootstrap.PortServicie']", 'on_delete': 'models.PROTECT'}),
            'ref_40': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        },
        'bootstrap.portservicie': {
            'Meta': {'object_name': 'PortServicie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bootstrap.Measure']", 'on_delete': 'models.PROTECT'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'nds': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bootstrap.Nds']", 'on_delete': 'models.PROTECT'})
        }
    }

    complete_apps = ['bootstrap']