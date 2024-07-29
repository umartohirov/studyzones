from django.contrib import admin
from .models import Place,Location
from .forms import LocationForm
# Register your models here.

admin.site.register(Place)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    form = LocationForm
    list_display = ('name', 'lat', 'lng')
    search_fields = ('name',)