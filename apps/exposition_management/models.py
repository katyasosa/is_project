from django.db import models
from django.utils.encoding import python_2_unicode_compatible


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

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Plant(models.Model):
    species = models.ForeignKey(PlantSpecies)

    def __str__(self):
        return str(self.species) + " plant"


@python_2_unicode_compatible
class Exposition(models.Model):
    STAGE_IDEA = 1
    STAGE_PLANT_SELECTION = 2
    STAGE_DESIGN = 3
    STAGE_VERIFICATION = 4
    STAGE_WAITING = 5
    STAGE_ACTIVE = 6
    STAGE_ARCHIVE = 7

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