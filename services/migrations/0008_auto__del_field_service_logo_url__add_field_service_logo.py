# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Service.logo_url'
        db.delete_column(u'services_service', 'logo_url')

        # Adding field 'Service.logo'
        db.add_column(u'services_service', 'logo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Service.logo_url'
        raise RuntimeError("Cannot reverse this migration. 'Service.logo_url' and its values cannot be restored.")
        # Deleting field 'Service.logo'
        db.delete_column(u'services_service', 'logo')


    models = {
        u'services.service': {
            'Meta': {'ordering': "('category',)", 'object_name': 'Service'},
            'badges': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'services'", 'symmetrical': 'False', 'to': u"orm['services.ServiceBadge']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services'", 'to': u"orm['services.ServiceCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'profile_url_template': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'services.servicebadge': {
            'Meta': {'object_name': 'ServiceBadge'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['services.ServiceBadgeCategory']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'picto': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'services.servicebadgecategory': {
            'Meta': {'object_name': 'ServiceBadgeCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'services.servicecategory': {
            'Meta': {'object_name': 'ServiceCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['services']