from django.urls import path
from .serial_views import LvStationData
from . import views
from . import serial_views
from djgeojson.views import GeoJSONLayerView

app_name = 'app_eGoVIS'

urlpatterns = [
    # path('', views.index, name='basemap'),
    # path('', views.basemap, name='index'),
    path('', views.basemap_template, name='index'),

    # 1 - Line
    path('Lines.data/', serial_views.LinesDataTest.as_view(), name='Lines.data'),
    #2 - LV
    path('LvBranchtee.data/', serial_views.LvBranchteeDataTest.as_view(), name='LvBranchtee.data'),
    #3
    path('LvGenerator.data/', serial_views.LvGeneratorDataTest.as_view(), name='LvGenerator.data'),
    #4
    path('LvGrid.data/', serial_views.LvGridDataTest.as_view(), name='LvGrid.data'),
    #5
    path('LvLoadarea.data/', serial_views.LvLoadareaDataTest.as_view(), name='LvLoadarea.data'),
    #6
    path('LvStation.data/', serial_views.LvStationDataTest.as_view(), name='LvStation.data'),
    #7 - MV
    path('MvBranchtee.data/', serial_views.MvBranchteeDataTest.as_view(), name='MvBranchtee.data'),
    #8
    path('MvCircuitbreaker.data/', serial_views.MvCircuitbreakerDataTest.as_view(), name='MvCircuitbreaker.data'),
    #9
    path('MvGenerator.data/', serial_views.MvGeneratorDataTest.as_view(), name='MvGenerator.data'),
    #10
    path('MvGrid.data/', serial_views.MvGridDataTest.as_view(), name='MvGrid.data'),
    #11
    path('MvLoad.data/', serial_views.MvLoadDataTest.as_view(), name='MvLoad.data'),
    #12
    path('MvStation.data/', serial_views.MvStationDataTest.as_view(), name='MvStation.data'),
    #13 - Transformer (Substation)
    path('HvmvTransformer.data/', serial_views.HvmvTransformerDataTest.as_view(), name='HvmvTransformer.data'),
    #14
    path('MvlvTransformer.data/', serial_views.MvlvTransformerDataTest.as_view(), name='MvlvTransformer.data'),
    #15 - Non Geometry
# path('LvGridData.data/', serial_views.LvGridDataTest.as_view(), name='LvGridData.data'),
#     #16
# path('LvGridData.data/', serial_views.LvGridDataTest.as_view(), name='LvGridData.data'),

]
