from __future__ import absolute_import

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from .forms import CrispyAuthenticationForm

admin.autodiscover()

urlpatterns = patterns('',
   url(r'^$',
       TemplateView.as_view(template_name='index.html'),
       name='main_page'),
   url(r'^about$', TemplateView.as_view(template_name='about.html'),
       name='about'),

   url(r'^accounts/login/$', 'django.contrib.auth.views.login',
       {'template_name': 'registration/login.html',
        'authentication_form': CrispyAuthenticationForm},
       name='login'),
   url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
       {'next_page': '/'},
       name='logout'),

   url(r'', include('exposition_management.urls')),
   url(r'^admin/', include(admin.site.urls))
) +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
