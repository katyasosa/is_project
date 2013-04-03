from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View
from django import forms
from django.views.generic.edit import ModelFormMixin
from django.forms.models import modelformset_factory

from .models import Exposition, Plant, PlantPosition


class AddExpositionForm(forms.ModelForm):
    class Meta:
        model = Exposition
        exclude = ['plants']


class AddPlantsToExpositionForm(forms.ModelForm):
    class Meta:
        model = Exposition
        fields = ['plants']


class PlantPositionForm(forms.ModelForm):
    class Meta:
        model = PlantPosition
        fields = ['plant', 'position_x', 'position_y']


PositionsFormSet = modelformset_factory(form=PlantPositionForm, extra=0,
                                        model=PlantPosition)


class EditExpositionMixin(object):
    def get_success_url(self):
        return reverse('exposition_detail',
                       kwargs={'pk': self.get_object().pk})


class CreateExpositionView(CreateView):
    model = Exposition
    template_name = 'exposition_management/create_exposition.html'
    form_class = AddExpositionForm

    def get_success_url(self):
        return reverse('exposition_list')


class AddPlantsToExpositionView(EditExpositionMixin, UpdateView):
    model = Exposition
    template_name = 'exposition_management/add_plants_to_exposition.html'
    form_class = AddPlantsToExpositionForm

    def form_valid(self, form):
        exposition = form.save(commit=False)

        plants = form.cleaned_data['plants']
        for p in plants:
            relation = PlantPosition(exposition=exposition, plant=p)
            relation.save()

        exposition.save()
        return super(ModelFormMixin, self).form_valid(form)


class EditPositionsView(EditExpositionMixin, View):

    def get(self, *args, **kwargs):
        exposition = Exposition.objects.get(pk=kwargs['pk'])
        formset = PositionsFormSet(queryset=exposition.plantposition_set.all())
        return render_to_response('exposition_management/move_plants.html', {
            "formset": formset,
        })

    def post(self, *args, **kwargs):
        pass


class ExpositionListView(ListView):
    model = Exposition
    template_name = 'exposition_management/exposition_list.html'


class ExpositionDetailView(DetailView):
    model = Exposition
    template_name = 'exposition_management/exposition_details.html'


class AddPlantForm(forms.ModelForm):
    class Meta:
        model = Plant


class AddPlantView(CreateView):
    model = Plant
    template_name = 'exposition_management/add_plant.html'
    form_class = AddPlantForm

    def get_success_url(self):
        return reverse('plant_list')


class PlantListView(ListView):
    model = Plant
    template_name = 'exposition_management/plant_list.html'