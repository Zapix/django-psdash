# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.MainView.as_view(), name='psdash_main'),
    url(r'^categories/$', views.MainView.as_view(), name='psdash_categories'),
)
