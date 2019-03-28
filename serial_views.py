from .models import *
from djgeojson.views import GeoJSONLayerView


#########################
### GeoJSONLayerViews ###
#########################

# run (run_id) in properties causes long loading time when displayed in browser


# class LinesData(GeoJSONLayerView):
#     model = EgoGridDing0LineTest
#     #properties = ['run', 'type_name', 'length', 'u_n', 'c', 'l', 'r', 'i_max_th']
#     properties = ['type_name', 'length', 'u_n', 'c', 'l', 'r', 'i_max_th']
#     srid = 4326
#     geometry_field = 'geom'
#
#
#
# #######  LV  #######
#
# class LvBranchteeData(GeoJSONLayerView):
#     model = EgoGridDing0LvBranchteeTest
#     properties = ['name']
#     srid = 4326
#     geometry_field = 'geom'
#     precision = 5
#
#
# class LvGeneratorData(GeoJSONLayerView):
#     model = EgoGridDing0LvGeneratorTest
#     properties = ['lv_grid_id', 'type', 'subtype', 'nominal_capacity', 'is_aggregated']
#     srid = 4326
#     geometry_field = 'geom'
#     precision = 5
#
#
# class LvGridData(GeoJSONLayerView):
#     model = EgoGridDing0LvGridTest
#     properties = ['population', 'voltage_nom']
#     srid = 4326
#     geometry_field = 'geom'
#     precision = 5
#
#
# class LvLoadareaData(GeoJSONLayerView):
#     model = EgoGridDing0LvLoadTest
#     properties = ['name', 'consumption']
#     srid = 4326
#     geometry_field = 'geom'
#     precision = 5
#
#
# class LvStationData(GeoJSONLayerView):
#     model = EgoGridDing0LvStationTest
#     properties = ['name']
#     srid = 4326
#     geometry_field = 'geom'
#     precision = 5
#
#
# #######  MV  #######
#
# class MvBranchteeData(GeoJSONLayerView):
#     model = EgoGridDing0MvBranchteeTest
#     properties = ['name']
#     srid = 4326
#     geometry_field = 'geom'
#     precision = 5
#
#
# class MvCircuitbreakerData(GeoJSONLayerView):
#     model = EgoGridDing0MvCircuitbreakerTest
#     properties = ['name', 'status']
#     srid = 4326
#     geometry_field = 'geom'
#     precision = 5
#
#
# class MvGeneratorData(GeoJSONLayerView):
#     model = EgoGridDing0MvGeneratorTest
#     properties = ['type', 'subtype', 'nominal_capacity', 'is_aggregated']
#     srid = 4326
#     geometry_field = 'geom'
#     precision = 5
#
#
# class MvGridData(GeoJSONLayerView):
#     model = EgoGridDing0MvGridTest
#     properties = ['population', 'voltage_nom']
#     srid = 4326
#     geometry_field = 'geom'
#     precision = 5
#
#
# class MvLoadData(GeoJSONLayerView):
#     model = EgoGridDing0MvLoadTest
#     properties = ['name', 'is_aggregated', 'consumption']
#     srid = 4326
#     geometry_field = 'geom'
#     precision = 5
#
#
# class MvStationData(GeoJSONLayerView):
#     model = EgoGridDing0MvStationTest
#     properties = ['name', 'run']
#     srid = 4326
#     geometry_field = 'geom'
#     precision = 5
#
#
# ##### Transformer ####
#
# class HvmvTransformerData(GeoJSONLayerView):
#     model = EgoGridDing0HvmvTransformerTest
#     properties = ['voltage_op', 's_nom', 'x', 'r']
#     srid = 4326
#     geometry_field = 'geom'
#     precision = 5
#
#
# class MvlvTransformerData(GeoJSONLayerView):
#     model = EgoGridDing0MvlvTransformerTest
#     properties = ['voltage_op', 's_nom', 'x', 'r']
#     srid = 4326
#     geometry_field = 'geom'
#     precision = 5
#
#
# ##### non Geometry ######
#
# class MvlvMappingData(GeoJSONLayerView):
#     model = EgoGridDing0MvlvMappingTest
#
# class Ding0VersioningData(GeoJSONLayerView):
#     model = EgoGridDing0VersioningTest

class LinesData(GeoJSONLayerView):
    model = EgoGridDing0Line
    #properties = ['run', 'type_name', 'length', 'u_n', 'c', 'l', 'r', 'i_max_th']
    properties = ['type_name', 'length', 'u_n', 'c', 'l', 'r', 'i_max_th']
    srid = 4326
    geometry_field = 'geom'



#######  LV  #######

class LvBranchteeData(GeoJSONLayerView):
    model = EgoGridDing0LvBranchtee
    properties = ['name']
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class LvGeneratorData(GeoJSONLayerView):
    model = EgoGridDing0LvGenerator
    properties = ['lv_grid_id', 'type', 'subtype', 'nominal_capacity', 'is_aggregated']
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class LvGridData(GeoJSONLayerView):
    model = EgoGridDing0LvGrid
    properties = ['population', 'voltage_nom']
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class LvLoadareaData(GeoJSONLayerView):
    model = EgoGridDing0LvLoad
    properties = ['name', 'consumption']
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class LvStationData(GeoJSONLayerView):
    model = EgoGridDing0LvStation
    properties = ['name']
    srid = 4326
    geometry_field = 'geom'
    precision = 5


#######  MV  #######

class MvBranchteeData(GeoJSONLayerView):
    model = EgoGridDing0MvBranchtee
    properties = ['name']
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class MvCircuitbreakerData(GeoJSONLayerView):
    model = EgoGridDing0MvCircuitbreaker
    properties = ['name', 'status']
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class MvGeneratorData(GeoJSONLayerView):
    model = EgoGridDing0MvGenerator
    properties = ['type', 'subtype', 'nominal_capacity', 'is_aggregated']
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class MvGridData(GeoJSONLayerView):
    model = EgoGridDing0MvGrid
    properties = ['population', 'voltage_nom']
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class MvLoadData(GeoJSONLayerView):
    model = EgoGridDing0MvLoad
    properties = ['name', 'is_aggregated', 'consumption']
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class MvStationData(GeoJSONLayerView):
    model = EgoGridDing0MvStation
    properties = ['name', 'run']
    srid = 4326
    geometry_field = 'geom'
    precision = 5


##### Transformer ####

class HvmvTransformerData(GeoJSONLayerView):
    model = EgoGridDing0HvmvTransformer
    properties = ['voltage_op', 's_nom', 'x', 'r']
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class MvlvTransformerData(GeoJSONLayerView):
    model = EgoGridDing0MvlvTransformer
    properties = ['voltage_op', 's_nom', 'x', 'r']
    srid = 4326
    geometry_field = 'geom'
    precision = 5


##### non Geometry ######

class MvlvMappingData(GeoJSONLayerView):
    model = EgoGridDing0MvlvMapping

class Ding0VersioningData(GeoJSONLayerView):
    model = EgoGridDing0Versioning




