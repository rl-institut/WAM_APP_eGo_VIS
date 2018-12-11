from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.



# class EgoGridDing0VersioningTest(models.Model):
#     run_id = models.BigIntegerField(primary_key=True)
#     description = models.CharField(max_length=6000, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ego_grid_ding0_versioning_test'
#
#
# class EgoGridDing0LvStationTest(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
#     id_db = models.BigIntegerField(blank=True, null=True)
#     geom = geomodels.PointField(blank=True, null=True)
#     name = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ego_grid_ding0_lv_station_test'
#
#         # plural form in admin view
#         verbose_name_plural = 'lv_station'
#
#     def init(self):
#         Lv_Station = EgoGridDing0LvStationTest()
#
#         return Lv_Station

class EgoGridDing0HvmvTransformerTest(models.Model):
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    id_db = models.BigIntegerField(blank=True, null=True)
    geom = geomodels.PointField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    voltage_op = models.FloatField(blank=True, null=True)
    s_nom = models.FloatField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    r = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_hvmv_transformer_test'

class EgoGridDing0LineTest(models.Model):
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    id_db = models.BigIntegerField(blank=True, null=True)
    edge_name = models.CharField(max_length=100, blank=True, null=True)
    grid_name = models.CharField(max_length=100, blank=True, null=True)
    node1 = models.CharField(max_length=100, blank=True, null=True)
    node2 = models.CharField(max_length=100, blank=True, null=True)
    type_kind = models.CharField(max_length=100, blank=True, null=True)
    type_name = models.CharField(max_length=100, blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    u_n = models.FloatField(blank=True, null=True)
    c = models.FloatField(blank=True, null=True)
    l = models.FloatField(blank=True, null=True)
    r = models.FloatField(blank=True, null=True)
    i_max_th = models.FloatField(blank=True, null=True)
    geom = geomodels.LineStringField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_line_test'

class EgoGridDing0LvBranchteeTest(models.Model):
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    id_db = models.BigIntegerField(blank=True, null=True)
    geom = geomodels.PointField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_lv_branchtee_test'

class EgoGridDing0LvGeneratorTest(models.Model):
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    id_db = models.BigIntegerField(blank=True, null=True)
    la_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    lv_grid_id = models.BigIntegerField(blank=True, null=True)
    geom = geomodels.PointField(blank=True, null=True)
    type = models.CharField(max_length=22, blank=True, null=True)
    subtype = models.CharField(max_length=30, blank=True, null=True)
    v_level = models.IntegerField(blank=True, null=True)
    nominal_capacity = models.FloatField(blank=True, null=True)
    weather_cell_id = models.BigIntegerField(blank=True, null=True)
    is_aggregated = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_lv_generator_test'

class EgoGridDing0LvGridTest(models.Model):
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    id_db = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = geomodels.MultiPolygonField(blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    voltage_nom = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_lv_grid_test'

class EgoGridDing0LvLoadTest(models.Model):
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    id_db = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    lv_grid_id = models.BigIntegerField(blank=True, null=True)
    geom = geomodels.PointField(blank=True, null=True)
    consumption = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_lv_load_test'

class EgoGridDing0LvStationTest(models.Model):
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    id_db = models.BigIntegerField(blank=True, null=True)
    geom = geomodels.PointField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_lv_station_test'

class EgoGridDing0MvBranchteeTest(models.Model):
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    id_db = models.BigIntegerField(blank=True, null=True)
    geom = geomodels.PointField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_mv_branchtee_test'

class EgoGridDing0MvCircuitbreakerTest(models.Model):
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    id_db = models.BigIntegerField(blank=True, null=True)
    geom = geomodels.PointField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_mv_circuitbreaker_test'

class EgoGridDing0MvGeneratorTest(models.Model):
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    id_db = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = geomodels.PointField(blank=True, null=True)
    type = models.CharField(max_length=22, blank=True, null=True)
    subtype = models.CharField(max_length=30, blank=True, null=True)
    v_level = models.IntegerField(blank=True, null=True)
    nominal_capacity = models.FloatField(blank=True, null=True)
    weather_cell_id = models.BigIntegerField(blank=True, null=True)
    is_aggregated = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_mv_generator_test'

class EgoGridDing0MvGridTest(models.Model):
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    id_db = models.BigIntegerField(blank=True, null=True)
    geom = geomodels.MultiPolygonField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    voltage_nom = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_mv_grid_test'

class EgoGridDing0MvLoadTest(models.Model):
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    id_db = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    geom = geomodels.GeometryField(blank=True, null=True)
    is_aggregated = models.BooleanField(blank=True, null=True)
    consumption = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_mv_load_test'

class EgoGridDing0MvStationTest(models.Model):
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    id_db = models.BigIntegerField(blank=True, null=True)
    geom = geomodels.PointField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_mv_station_test'

class EgoGridDing0MvlvMappingTest(models.Model):
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    lv_grid_id = models.BigIntegerField(blank=True, null=True)
    lv_grid_name = models.CharField(max_length=100, blank=True, null=True)
    mv_grid_id = models.BigIntegerField(blank=True, null=True)
    mv_grid_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_mvlv_mapping_test'

class EgoGridDing0MvlvTransformerTest(models.Model):
    run = models.ForeignKey('EgoGridDing0VersioningTest', models.DO_NOTHING)
    id_db = models.BigIntegerField(blank=True, null=True)
    geom = geomodels.PointField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    voltage_op = models.FloatField(blank=True, null=True)
    s_nom = models.FloatField(blank=True, null=True)
    x = models.FloatField(blank=True, null=True)
    r = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_mvlv_transformer_test'

class EgoGridDing0VersioningTest(models.Model):
    run_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=6000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ego_grid_ding0_versioning_test'
