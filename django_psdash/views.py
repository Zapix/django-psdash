# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'psdash/index.html'