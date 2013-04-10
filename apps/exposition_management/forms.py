from __future__ import absolute_import, unicode_literals

from django import forms
from django.forms.models import modelformset_factory

from .models import Exposition, Plant, PlantPosition


class ExpositionForm(forms.ModelForm):
    class Meta:
        model = Exposition
        exclude = ['plants', 'stage']


class EditExpositionForm(forms.ModelForm):
    class Meta:
        model = Exposition
        fields = ['plants']


class PlantPositionForm(forms.ModelForm):
    class Meta:
        model = PlantPosition
        fields = ['position_x', 'position_y']


PositionsFormSet = modelformset_factory(
    form=PlantPositionForm, extra=0, model=PlantPosition)


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
