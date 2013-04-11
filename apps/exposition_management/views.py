from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import ModelFormMixin

from extra_views import ModelFormSetView

from .forms import ExpositionForm, EditExpositionForm, \
     PositionsFormSet, PlantForm
from .models import Exposition, Plant, PlantPosition, Room


class EditExpositionMixin(object):
    def get_success_url(self):
        return reverse('exposition_detail',
                       kwargs={'pk': self.get_object().pk})


class CreateExpositionView(CreateView):
    model = Exposition
    template_name = 'exposition_management/create_exposition.html'
    form_class = ExpositionForm

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
    form_class = EditExpositionForm

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

    def get_context_data(self, **kwargs):
        room = Exposition.objects.get(pk=self.kwargs['pk']).room
        context = {'room': room}
        context.update(**kwargs)

        return super(EditPositionsView, self).get_context_data(**context)


class ExpositionListView(ListView):
    model = Exposition


class ExpositionDetailView(DetailView):
    model = Exposition


class AddPlantView(CreateView):
    model = Plant
    form_class = PlantForm

    def get_success_url(self):
        return reverse('plant_list')


class PlantListView(ListView):
    model = Plant
