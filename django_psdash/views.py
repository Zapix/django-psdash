# -*- coding: utf-8 -*-
import json

from django import http
from django.views import generic as cbv
from django.conf import settings

from .utils import import_function
from .utils import check_settings
from .settings import DJANGO_PSDASH_CATEGORIES


class PermissionCheckerMixin(object):

    def dispatch(self, request, *args, **kwargs):
        check_settings(DJANGO_PSDASH_CATEGORIES)
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


class JsonResponseMixin(object):

    def render_to_response(self, data):

        return http.HttpResponse(
            content=json.dumps(data),
            content_type='application/json'
        )


class MainView(PermissionCheckerMixin, cbv.TemplateView):
    template_name = 'psdash/index.html'


class GetCategoriesView(JsonResponseMixin, PermissionCheckerMixin,
                            cbv.View):

    def get(self, request, *args, **kwargs):
        return self.render_to_response(
            {
                key: value['name']
                for key, value in DJANGO_PSDASH_CATEGORIES.iteritems()
            }
        )
