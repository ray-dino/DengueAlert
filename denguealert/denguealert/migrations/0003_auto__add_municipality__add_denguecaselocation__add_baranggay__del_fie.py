# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Municipality'
        db.create_table(u'denguealert_municipality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True, blank=True)),
            ('area', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'denguealert', ['Municipality'])

        # Adding model 'DengueCaseLocation'
        db.create_table(u'denguealert_denguecaselocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dengue_case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['denguealert.DengueCase'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'denguealert', ['DengueCaseLocation'])

        # Adding model 'Baranggay'
        db.create_table(u'denguealert_baranggay', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=2048, null=True, blank=True)),
            ('municipality', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['denguealert.Municipality'])),
            ('area', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'denguealert', ['Baranggay'])

        # Deleting field 'DengueCase.point'
        db.delete_column(u'denguealert_denguecase', 'point')

        # Deleting field 'DengueCase.longitude'
        db.delete_column(u'denguealert_denguecase', 'longitude')

        # Deleting field 'DengueCase.latitude'
        db.delete_column(u'denguealert_denguecase', 'latitude')

        # Deleting field 'DengueCase.address'
        db.delete_column(u'denguealert_denguecase', 'address')

        # Deleting field 'DengueCase.date'
        db.delete_column(u'denguealert_denguecase', 'date')

        # Adding field 'DengueCase.patient_name'
        db.add_column(u'denguealert_denguecase', 'patient_name',
                      self.gf('django.db.models.fields.CharField')(max_length=2048, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DengueCase.created_date'
        db.add_column(u'denguealert_denguecase', 'created_date',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.datetime(2014, 5, 4, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'DengueCase.onset_date'
        db.add_column(u'denguealert_denguecase', 'onset_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 5, 4, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Municipality'
        db.delete_table(u'denguealert_municipality')

        # Deleting model 'DengueCaseLocation'
        db.delete_table(u'denguealert_denguecaselocation')

        # Deleting model 'Baranggay'
        db.delete_table(u'denguealert_baranggay')

        # Adding field 'DengueCase.point'
        db.add_column(u'denguealert_denguecase', 'point',
                      self.gf('django.contrib.gis.db.models.fields.PointField')(default=0),
                      keep_default=False)

        # Adding field 'DengueCase.longitude'
        db.add_column(u'denguealert_denguecase', 'longitude',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'DengueCase.latitude'
        db.add_column(u'denguealert_denguecase', 'latitude',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'DengueCase.address'
        db.add_column(u'denguealert_denguecase', 'address',
                      self.gf('django.db.models.fields.CharField')(max_length=2048, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DengueCase.date'
        db.add_column(u'denguealert_denguecase', 'date',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.datetime(2014, 5, 4, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'DengueCase.patient_name'
        db.delete_column(u'denguealert_denguecase', 'patient_name')

        # Deleting field 'DengueCase.created_date'
        db.delete_column(u'denguealert_denguecase', 'created_date')

        # Deleting field 'DengueCase.onset_date'
        db.delete_column(u'denguealert_denguecase', 'onset_date')


    models = {
        u'denguealert.baranggay': {
            'Meta': {'object_name': 'Baranggay'},
            'area': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipality': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['denguealert.Municipality']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'})
        },
        u'denguealert.denguecase': {
            'Meta': {'object_name': 'DengueCase'},
            'created_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'onset_date': ('django.db.models.fields.DateField', [], {}),
            'patient_name': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'})
        },
        u'denguealert.denguecaselocation': {
            'Meta': {'object_name': 'DengueCaseLocation'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'dengue_case': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['denguealert.DengueCase']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {})
        },
        u'denguealert.municipality': {
            'Meta': {'object_name': 'Municipality'},
            'area': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['denguealert']