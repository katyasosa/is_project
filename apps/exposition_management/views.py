from django.views.generic import CreateView
from django import forms

from .models import Exposition


class AddExpositionForm(forms.ModelForm):

    class Meta:
        model = Exposition

class CreateExpositionView(CreateView):
    model = Exposition
    template_name = 'exposition_management/create_exposition.html'
    form_class = AddExpositionForm