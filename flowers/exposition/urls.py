from django.conf.urls import patterns, url
from django.views.generic import ListView, TemplateView
from exposition.models import Exposition
from exposition.views import create_exposition

urlpatterns = patterns('',
                       url(r'^list/$', ListView.as_view(
                           queryset=Exposition.objects.all,
                           template_name='exposition_list.html')),
                       url(r'^create_exposition/$', create_exposition))


