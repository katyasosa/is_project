# coding=utf-8
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import ImproperlyConfigured
from django.utils.encoding import force_str
from django.shortcuts import resolve_url


class LoginRequiredMiddleware(object):
    def process_request(self, request):
        if not hasattr(request, 'user'):
            raise ImproperlyConfigured(
                "The Django remote user auth middleware requires the"
                " authentication middleware to be installed.  Edit your"
                " MIDDLEWARE_CLASSES setting to insert"
                " 'django.contrib.auth.middleware.AuthenticationMiddleware'"
                " before the LoginRequiredMiddleware class.")

        resolved_login_url = force_str(resolve_url(settings.LOGIN_URL))
        if (not request.user.is_authenticated() and
            request.path != resolved_login_url):
            path = request.build_absolute_uri()
            return redirect_to_login(
                path, resolved_login_url, REDIRECT_FIELD_NAME)
