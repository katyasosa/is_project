from django.conf.urls import patterns, url

from .views import CreateExpositionView, ExpositionListView, \
    ExpositionDetailView, PlantListView, AddPlantView, \
    AddPlantsToExpositionView

urlpatterns = patterns('',
   url(r'^expositions/$', ExpositionListView.as_view(),
       name='exposition_list'),
   url(r'^expositions/create/$', CreateExpositionView.as_view(),
       name='create_exposition'),
   url(r'^expositions/(?P<pk>\d+)/$', ExpositionDetailView.as_view(),
       name='exposition_detail'),

   url(r'^expositions/(?P<pk>\d+)/add-plants$',
       AddPlantsToExpositionView.as_view(),
       name='add_plants_to_exposition'),

   url(r'^plants/$', PlantListView.as_view(),
       name='plant_list'),
   url(r'^plants/add/$', AddPlantView.as_view(),
       name='add_plant')


)


