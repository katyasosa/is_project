from __future__ import absolute_import, unicode_literals

import posixpath

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.conf import settings
from django.forms.models import modelformset_factory
from django.utils.html import conditional_escape, mark_safe

from .models import Exposition, Plant, PlantPosition, PlantSpecies


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


class SpeciesChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        if obj.image:
            image = conditional_escape(obj.image.url_200x200)
        else:
            image = "http://placekitten.com/200/200"

        title = conditional_escape(obj.name)
        return mark_safe(
            """<span class="thumbnail">
                 <img src="{0}" alt="{1}" />
                 <span class="caption">{1}</span>
               </span>""".format(image, title))


class PlantForm(forms.ModelForm):
    species = SpeciesChoiceField(PlantSpecies.objects.all(),
        empty_label=None, widget=forms.RadioSelect)

    class Meta:
        model = Plant

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        super(PlantForm, self).__init__(*args, **kwargs)
