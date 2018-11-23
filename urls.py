from django.urls import path
from .serial_views import LvStationData
from . import views
from . import serial_views
from djgeojson.views import GeoJSONLayerView

app_name = 'app_eGoVIS'

urlpatterns = [
    # path('', views.index, name='basemap'),
    path('', views.basemap, name='index'),
    # path('app_eGoVIS/basemap', views.get_data, name='features'),
    # path(r'^LvStationData.data/', GeoJSONLayerView.as_view(model=LvStationData), name='data')
    path('LvStation.data/', serial_views.LvStationData.as_view(), name='LvStation.data')
]