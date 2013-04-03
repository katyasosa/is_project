from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django import forms

from .models import Exposition


class AddExpositionForm(forms.ModelForm):

    class Meta:
        model = Exposition
        exclude = ['plants']

class CreateExpositionView(CreateView):
    model = Exposition
    template_name = 'exposition_management/create_exposition.html'
    form_class = AddExpositionForm

    def get_success_url(self):
        return reverse('exposition_list')