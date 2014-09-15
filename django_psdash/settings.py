# -*- coding: utf-8 -*-
from django.conf import settings


DJANGO_PSDASH_CATEGORIES = getattr(
    settings,
    'DJANGO_PSDASH_CATEGORIES',
    {
        'overview': {
            'name': 'Overview',
            'icon-class': '',
            'panels': []
        },
        'processes': {
            'name': 'Processes',
            'icon-class': '',
            'panels': []
        }
    }
)
