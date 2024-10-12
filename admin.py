from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Clinics,Wards,Hospitals

class clinicsAdmin(LeafletGeoAdmin):
    list_display=('name',)
admin.site.register(Clinics,clinicsAdmin)

class wardsAdmin(LeafletGeoAdmin):
    list_display=('admin3name',)
admin.site.register(Wards,wardsAdmin) 

class hospitalsAdmin(LeafletGeoAdmin):
    list_display=('name',)
admin.site.register(Hospitals,hospitalsAdmin)    