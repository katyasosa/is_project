from django.db import models
import itertools


class Room(models.Model):
    area = models.IntegerField()


class PlantSpecies(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Plant(models.Model):
    species = models.ForeignKey(PlantSpecies)


class Exposition(models.Model):
    STAGE_IDEA = 1

    name = models.CharField(max_length=100)
    description = models.TextField()
    room = models.ForeignKey(Room)
    stage = models.SmallIntegerField(choices=[(STAGE_IDEA, 'Idea')])
    begin = models.DateField()
    end = models.DateField()
    plants = models.ManyToManyField(Plant)


