# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import mark_safe
from django_thumbs.db.models import ImageWithThumbsField


class PreviewMixin(object):
    @property
    def preview_url(self):
        return mark_safe(self.image.url_200x200 if self.image else
                         "http://placekitten.com/200/200")


@python_2_unicode_compatible
class Room(models.Model, PreviewMixin):
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    image = ImageWithThumbsField(upload_to='room_images', sizes=[(200, 200)])

    def __str__(self):
        return '{0} x {1} room'.format(self.width, self.height)


@python_2_unicode_compatible
class PlantSpecies(models.Model, PreviewMixin):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = ImageWithThumbsField(
        upload_to='plant_species', sizes=[(200, 200)], blank=True, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Plant(models.Model):
    species = models.ForeignKey(PlantSpecies)

    @property
    def preview_url(self):
        return self.species.preview_url

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
     STAGE_ARCHIVED) = range(1, 8)

    name = models.CharField(max_length=100)
    description = models.TextField()
    room = models.ForeignKey(Room)
    stage = models.SmallIntegerField(editable=False, choices=[
        (STAGE_IDEA, 'Idea'),
        (STAGE_PLANT_SELECTION, 'Plant selection'),
        (STAGE_DESIGN, 'Design'),
        (STAGE_VERIFICATION, 'Verification'),
        (STAGE_WAITING, 'Waiting'),
        (STAGE_ACTIVE, 'Active'),
        (STAGE_ARCHIVED, 'Archive'),
    ])
    opening_date = models.DateField()
    closing_date = models.DateField()
    plants = models.ManyToManyField(Plant, through='PlantPosition')

    def __str__(self):
        return self.name


class PlantPosition(models.Model):
    plant = models.ForeignKey(Plant)
    exposition = models.ForeignKey(Exposition)

    position_x = models.PositiveIntegerField(default=0)
    position_y = models.PositiveIntegerField(default=0)


# A hack to make 'South' work with 'ImageWithThumbsField'.
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], [r"^django_thumbs.db.models.ImageWithThumbsField"])
