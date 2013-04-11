from django import template
from exposition_management.models import PlantPosition, Plant

register = template.Library()


@register.inclusion_tag('exposition_management/room_with_plants.html')
def draw_exposition_room(exposition, callback):
    context = {'callback': callback,
               'room': exposition.room}

    plant_positions = PlantPosition.objects.filter(exposition=exposition)
    context['plants'] = [
        {
            'id': p.plant.id,
            'x': p.position_x,
            'y': p.position_y,
            'image_url': p.plant.species.preview_url
        }
        for p in plant_positions
    ]

    return context