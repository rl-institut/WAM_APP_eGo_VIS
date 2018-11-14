from django.http import HttpResponse
from django.template import Context, loader
from .models import EgoGridDing0LvStationTest
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.core.serializers import serialize
import json


def index(request):
    return HttpResponse("Hello, world. You're at the Maps index.")


def basemap(request):
    template = loader.get_template("app_eGoVIS/basemap.html")
    return HttpResponse(template.render)


def get_data():
    LvStation = EgoGridDing0LvStationTest()
    lvs_table = LvStation.objects.all()


def get_model_as_json():
    template_name = 'templates/basemap.html'

    LvStation = EgoGridDing0LvStationTest()
    lvs_table = LvStation.objects.all()

    # lvs_geojson = GeoJSONSerializer().serialize(LvStation, use_natural_keys=True, with_modelname=False)
    # lvs_geom_geojson = serialize('geojson', LvStation, fields=('geom'))



def render_geom(request):
    pass