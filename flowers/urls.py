from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='main_page'),
    url(r'^users/', include('employees.urls')),
    url(r'^exposition/', include('exposition.urls')),
    url(r'^admin/', include(admin.site.urls))
)
