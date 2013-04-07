from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django import forms
from django.views.generic.edit import ModelFormMixin
from django.forms.models import modelformset_factory

from extra_views import ModelFormSetView

from .models import Exposition, Plant, PlantPosition


class AddExpositionForm(forms.ModelForm):
    class Meta:
        model = Exposition
        exclude = ['plants', 'stage']


class AddPlantsToExpositionForm(forms.ModelForm):
    class Meta:
        model = Exposition
        fields = ['plants']


class PlantPositionForm(forms.ModelForm):
    class Meta:
        model = PlantPosition
        fields = ['position_x', 'position_y']


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

    def form_valid(self, form):
        exposition = form.save(commit=False)
        exposition.stage = Exposition.STAGE_IDEA
        exposition.save()
        return super(ModelFormMixin, self).form_valid(form)


    def get_success_url(self):
        return reverse('exposition_list')


class AddPlantsToExpositionView(EditExpositionMixin, UpdateView):
    model = Exposition
    template_name = 'exposition_management/add_plants_to_exposition.html'
    form_class = AddPlantsToExpositionForm

    def form_valid(self, form):
        exposition = form.save(commit=False)

        plants = form.cleaned_data['plants']
        PlantPosition.objects.filter(exposition=exposition).delete()
        for p in plants:
            relation = PlantPosition(exposition=exposition, plant=p)
            relation.save()

        exposition.save()
        return super(ModelFormMixin, self).form_valid(form)


class EditPositionsView(ModelFormSetView):
    template_name = 'exposition_management/move_plants.html'
    model = PlantPosition

    def get_queryset(self):
        pk = self.kwargs['pk']
        return super(EditPositionsView, self).get_queryset().filter(
            exposition=pk)

    def get_formset(self):
        return PositionsFormSet


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