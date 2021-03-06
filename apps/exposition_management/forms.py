# coding=utf-8
from __future__ import absolute_import, unicode_literals

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from django import forms
from django.forms.models import modelformset_factory

from .fields import ImageChoiceField, ImageMultipleChoiceField
from .models import Exposition, Room, Plant, PlantPosition, PlantSpecies
from .widgets import ImagePicker, MultipleImagePicker


class ExpositionForm(forms.ModelForm):
    room = ImageChoiceField(Room.objects.all(), widget=ImagePicker)

    class Meta:
        model = Exposition
        exclude = ['plants']

    def __init__(self, *args, **kwargs):
        super(ExpositionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        if self.initial:
            self.helper.add_input(Submit('submit', 'Save'))
        else:
            self.helper.add_input(Submit('submit', 'Add'))


class EditExpositionForm(forms.ModelForm):
    plants = ImageMultipleChoiceField(
        Plant.objects.all(), widget=MultipleImagePicker)

    class Meta:
        model = Exposition
        fields = ['plants']

    def __init__(self, *args, **kwargs):
        super(EditExpositionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        if self.initial:
            self.helper.add_input(Submit('submit', 'Save'))
        else:
            self.helper.add_input(Submit('submit', 'Add'))


class PlantPositionForm(forms.ModelForm):
    class Meta:
        model = PlantPosition
        fields = ['position_x', 'position_y']


PositionsFormSet = modelformset_factory(
    form=PlantPositionForm, extra=0, model=PlantPosition)


class PlantForm(forms.ModelForm):
    species = ImageChoiceField(PlantSpecies.objects.all(), widget=ImagePicker)

    class Meta:
        model = Plant

    def __init__(self, *args, **kwargs):
        super(PlantForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        if self.initial:
            self.helper.add_input(Submit('submit', 'Save'))
        else:
            self.helper.add_input(Submit('submit', 'Add'))
