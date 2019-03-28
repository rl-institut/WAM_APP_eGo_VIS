from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import *

# Register your models here.
admin.site.register(EgoGridDing0Versioning)
admin.site.register(EgoGridDing0LvStation, LeafletGeoAdmin)
