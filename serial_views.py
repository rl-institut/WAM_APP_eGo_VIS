from .models import EgoGridDing0LvStationTest as LvStation
from djgeojson.views import GeoJSONLayerView

#########################
### GeoJSONLayerViews ###
#########################

class LvStationData(GeoJSONLayerView):
    model = LvStation
    properties = ['popup_content', 'name']
    srid = 4326
    geometry_field = 'geom'
    precision = 5