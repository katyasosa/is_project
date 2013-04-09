from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from django.views.generic import TemplateView
from florida import settings

admin.autodiscover()

urlpatterns = patterns('',
   url(r'^$',
       TemplateView.as_view(template_name='index.html'),
       name='main_page'),

   url(r'^login$', 'django.contrib.auth.views.login',
       {'template_name': 'registration/login.html'},
       name='login'),

   url(r'^logout/$', 'django.contrib.auth.views.logout',
       {'next_page': '/'},
       name='logout'),

   url(r'', include('exposition_management.urls')),
   url(r'^admin/', include(admin.site.urls))
) +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
