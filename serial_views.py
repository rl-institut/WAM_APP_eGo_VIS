from .models import EgoGridDing0LvStationTest
from django.views.generic import TemplateView
# from djgeojson.views import GeoJSONLayerView
from django.core.serializers import serialize
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from djgeojson.views import GeoJSONLayerView
from djgeojson.serializers import Serializer as GeoJSONSerializer


#########################
### GeoJSONLayerViews ###
#########################

class LvStationData(GeoJSONLayerView):
    model = EgoGridDing0LvStationTest
    properties = ['name', 'run']
    srid = 4326
    geometry_field = 'geom'
    precision = 5



