# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ServiceCategory'
        db.create_table(u'services_servicecategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'services', ['ServiceCategory'])

        # Adding model 'ServiceBadge'
        db.create_table(u'services_servicebadge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'services', ['ServiceBadge'])

        # Adding model 'Service'
        db.create_table(u'services_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('logo_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('profile_url_template', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='services', to=orm['services.ServiceCategory'])),
        ))
        db.send_create_signal(u'services', ['Service'])

        # Adding M2M table for field badges on 'Service'
        m2m_table_name = db.shorten_name(u'services_service_badges')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('service', models.ForeignKey(orm[u'services.service'], null=False)),
            ('servicebadge', models.ForeignKey(orm[u'services.servicebadge'], null=False))
        ))
        db.create_unique(m2m_table_name, ['service_id', 'servicebadge_id'])


    def backwards(self, orm):
        # Deleting model 'ServiceCategory'
        db.delete_table(u'services_servicecategory')

        # Deleting model 'ServiceBadge'
        db.delete_table(u'services_servicebadge')

        # Deleting model 'Service'
        db.delete_table(u'services_service')

        # Removing M2M table for field badges on 'Service'
        db.delete_table(db.shorten_name(u'services_service_badges'))


    models = {
        u'services.service': {
            'Meta': {'ordering': "('category',)", 'object_name': 'Service'},
            'badges': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['services.ServiceBadge']", 'symmetrical': 'False'}),
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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'services.servicecategory': {
            'Meta': {'object_name': 'ServiceCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['services']