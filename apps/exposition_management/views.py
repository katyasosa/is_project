from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django import forms
from django.views.generic.edit import ModelFormMixin

from .models import Exposition, Plant, PlantPosition


class AddExpositionForm(forms.ModelForm):
    class Meta:
        model = Exposition
        exclude = ['plants']


class AddPlantsToExpositionForm(forms.ModelForm):
    class Meta:
        model = Exposition
        fields = ['plants']


class CreateExpositionView(CreateView):
    model = Exposition
    template_name = 'exposition_management/create_exposition.html'
    form_class = AddExpositionForm

    def get_success_url(self):
        return reverse('exposition_list')


class AddPlantsToExpositionView(UpdateView):
    model = Exposition
    template_name = "exposition_management/add_plants_to_exposition.html"
    form_class = AddPlantsToExpositionForm

    def form_valid(self, form):
        exposition = form.save(commit=False)

        plants = form.cleaned_data['plants']
        for p in plants:
            relation = PlantPosition(exposition=exposition, plant=p)
            relation.save()

        exposition.save()
        return super(ModelFormMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse('exposition_detail',
                       kwargs={'pk': self.get_object().pk})


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