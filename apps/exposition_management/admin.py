from django.contrib import admin

from .models import Exposition, Room, PlantSpecies, Plant

admin.site.register(Exposition)
admin.site.register(Room)
admin.site.register(PlantSpecies)
admin.site.register(Plant)
