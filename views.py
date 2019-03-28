from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from .models import EgoGridDing0LvStation
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.core.serializers import serialize
import json


def basemap_template(request):
    template = loader.get_template("app_eGoVIS/test_map_layout.html")
    return render(request, 'app_eGoVIS/test_map_layout.html')


def basemap(request):
    template = loader.get_template("app_eGoVIS/basemap.html")
    return render(request, 'app_eGoVIS/basemap.html')


# def get_data(request):
#     template = loader.get_template("template/app_eGoVIS/basemap.html")
#     lvs_table = EgoGridDing0LvStationTest.objects.all()
#
#     # lvs_json = serialize('geojson', lvs_table,
#     #            fields=('geom',))
#
#     # features = lvs_table
#
#     features = GeoJSONSerializer().serialize(lvs_table, use_natural_keys=True, with_modelname=False)
#     print(features)
#
#     # return HttpResponse(template.render('feature': lvs_table, request))
#     return render(request, 'app_eGoVIS/basemap.html', {'features': features})


# def get_model_as_json():
#     template_name = 'templates/basemap.html'
#
#     LvStation = EgoGridDing0LvStationTest()
#     lvs_table = LvStation.objects.all()
#
#     # lvs_geojson = GeoJSONSerializer().serialize(LvStation, use_natural_keys=True, with_modelname=False)
#     # lvs_geom_geojson = serialize('geojson', LvStation, fields=('geom'))

