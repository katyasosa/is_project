from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django_thumbs.db.models import ImageWithThumbsField


@python_2_unicode_compatible
class Room(models.Model):
    area = models.IntegerField()
    image = models.ImageField(upload_to='room_images')

    def __str__(self):
        return unicode(self.area) + u' area room'


@python_2_unicode_compatible
class PlantSpecies(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = ImageWithThumbsField(
        upload_to='plant_species', sizes=[(200, 200)], blank=True, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Plant(models.Model):
    species = models.ForeignKey(PlantSpecies)

    def __str__(self):
        return str(self.species) + " plant"


@python_2_unicode_compatible
class Exposition(models.Model):
    (STAGE_IDEA,
     STAGE_PLANT_SELECTION,
     STAGE_DESIGN,
     STAGE_VERIFICATION,
     STAGE_WAITING,
     STAGE_ACTIVE,
     STAGE_ARCHIVE) = range(1, 8)

    name = models.CharField(max_length=100)
    description = models.TextField()
    room = models.ForeignKey(Room)
    stage = models.SmallIntegerField(choices=[
        (STAGE_IDEA, 'idea'),
        (STAGE_PLANT_SELECTION, 'plant-selection'),
        (STAGE_DESIGN, 'design'),
        (STAGE_VERIFICATION, 'verification'),
        (STAGE_WAITING, 'waiting'),
        (STAGE_ACTIVE, 'active'),
        (STAGE_ARCHIVE, 'archive'),
    ])
    begin = models.DateField()
    end = models.DateField()
    plants = models.ManyToManyField(Plant, through='PlantPosition')

    def __str__(self):
        return self.name


class PlantPosition(models.Model):
    plant = models.ForeignKey(Plant)
    exposition = models.ForeignKey(Exposition)

    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)


# A hack to make 'South' work with 'ImageWithThumbsField'.
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], [r"^django_thumbs.db.models.ImageWithThumbsField"])
