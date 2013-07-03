# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ServiceBadgeCategory'
        db.create_table(u'services_servicebadgecategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'services', ['ServiceBadgeCategory'])

        # Adding field 'ServiceBadge.category'
        db.add_column(u'services_servicebadge', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['services.ServiceBadgeCategory']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ServiceBadgeCategory'
        db.delete_table(u'services_servicebadgecategory')

        # Deleting field 'ServiceBadge.category'
        db.delete_column(u'services_servicebadge', 'category_id')


    models = {
        u'services.service': {
            'Meta': {'ordering': "('category',)", 'object_name': 'Service'},
            'badges': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'services'", 'symmetrical': 'False', 'to': u"orm['services.ServiceBadge']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services'", 'to': u"orm['services.ServiceCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'profile_url_template': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'services.servicebadge': {
            'Meta': {'object_name': 'ServiceBadge'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['services.ServiceBadgeCategory']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'services.servicebadgecategory': {
            'Meta': {'object_name': 'ServiceBadgeCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'services.servicecategory': {
            'Meta': {'object_name': 'ServiceCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['services']