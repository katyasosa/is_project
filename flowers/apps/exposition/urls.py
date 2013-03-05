from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from exposition.models import Exposition
from exposition.views import create_exposition

urlpatterns = patterns('',
                       url(r'^list/$',
                           ListView.as_view(
                               queryset=Exposition.objects.all(),
                               template_name='exposition/exposition_list.html'),
                           name='exposition_list'),
                       url(r'^create_exposition/$', create_exposition),
                       url(r'^(?P<pk>\d+)/$',
                           DetailView.as_view(model=Exposition, template_name='exposition/exposition_details.html'),
                           name="exposition_detail"))


