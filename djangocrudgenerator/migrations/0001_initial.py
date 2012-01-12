# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Modelname'
        db.create_table('appname_modelname', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dni', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('appname', ['Modelname'])


    def backwards(self, orm):
        
        # Deleting model 'Modelname'
        db.delete_table('appname_modelname')


    models = {
        'appname.modelname': {
            'Meta': {'object_name': 'Modelname'},
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['appname']
