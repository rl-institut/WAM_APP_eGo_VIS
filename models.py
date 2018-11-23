from django.db import models

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models as geomodels


class EgoGridDing0VersioningTest(models.Model):
    run_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=6000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_versioning_test'


class EgoGridDing0LvStationTest(models.Model):
    id = models.BigIntegerField(primary_key=True)
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    id_db = models.BigIntegerField(blank=True, null=True)
    geom = geomodels.PointField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_lv_station_test'

        # plural form in admin view
        verbose_name_plural = 'lv_station'

    def init(self):
        Lv_Station = EgoGridDing0LvStationTest()

        return Lv_Station