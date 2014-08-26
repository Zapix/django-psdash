# -*- coding: utf-8 -*-
from django import http
from django.views.generic import TemplateView
from django.conf import settings

from .utils import import_function


class PermissionCheckerMixin(object):

    def dispatch(self, request, *args, **kwargs):
        checker_addr = getattr(settings, 'PSDASH_PERMISSION_CHECKER', None)

        if checker_addr is None:
            checker = lambda r: r.user.is_authenticated and r.user.is_superuser
        else:
            checker = import_function(checker_addr)

        if checker(request):
            return super(PermissionCheckerMixin, self).dispatch(
                request, *args, **kwargs
            )
        else:
            return http.HttpResponseForbidden("You haven't got access")


class MainView(PermissionCheckerMixin, TemplateView):
    template_name = 'psdash/index.html'
