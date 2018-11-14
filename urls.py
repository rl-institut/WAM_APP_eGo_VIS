from django.urls import path

from . import views

app_name = 'app_eGoVIS'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.basemap, name='basemap'),
    path('', views.get_data, name='geom')
]