from .models import *
from djgeojson.views import GeoJSONLayerView


#########################
### GeoJSONLayerViews ###
#########################


class LinesData(GeoJSONLayerView):
    model = EgoGridDing0LineTest


#######  LV  #######

class LvBranchteeData(GeoJSONLayerView):
    model = EgoGridDing0LvBranchteeTest
    properties = []
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class LvGeneratorData(GeoJSONLayerView):
    model = EgoGridDing0LvGeneratorTest
    properties = []
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class LvGridData(GeoJSONLayerView):
    model = EgoGridDing0LvGridTest
    properties = []
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class LvLoadareaData(GeoJSONLayerView):
    model = EgoGridDing0LvLoadTest
    properties = []
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class LvStationData(GeoJSONLayerView):
    model = EgoGridDing0LvStationTest
    properties = ['name', 'run']
    srid = 4326
    geometry_field = 'geom'
    precision = 5


#######  MV  #######

class MvBranchteeData(GeoJSONLayerView):
    model = EgoGridDing0MvBranchteeTest
    properties = []
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class MvCircuitbreakerData(GeoJSONLayerView):
    model = EgoGridDing0MvCircuitbreakerTest
    properties = []
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class MvGeneratorData(GeoJSONLayerView):
    model = EgoGridDing0MvGeneratorTest
    properties = []
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class MvGridData(GeoJSONLayerView):
    model = EgoGridDing0MvGridTest
    properties = []
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class MvLoadData(GeoJSONLayerView):
    model = EgoGridDing0MvLoadTest
    properties = []
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class MvStationData(GeoJSONLayerView):
    model = EgoGridDing0MvStationTest
    properties = []
    srid = 4326
    geometry_field = 'geom'
    precision = 5


##### Transformer ####

class HvmvTransformerData(GeoJSONLayerView):
    model = EgoGridDing0HvmvTransformerTest
    properties = []
    srid = 4326
    geometry_field = 'geom'
    precision = 5


class MvlvTransformerData(GeoJSONLayerView):
    model = EgoGridDing0MvlvTransformerTest
    srid = 4326
    geometry_field = 'geom'
    precision = 5


##### non Geometry ######

class MvlvMappingData(GeoJSONLayerView):
    model = EgoGridDing0MvlvMappingTest

class Ding0VersioningData(GeoJSONLayerView):
    model = EgoGridDing0VersioningTest



