from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'employees/login.html'},
                           name='login_form'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout'))
