# -*- coding: utf-8 -*-
import inspect
from collections import Iterable

from django.utils.importlib import import_module


def import_function(func_addr):
    module_addr = '.'.join(func_addr.split('.')[:-1])
    func_name = func_addr.split('.')[-1]

    try:
        module = import_module(module_addr)
    except (TypeError, ImportError):
        raise ValueError("Can't find function %s" % func_addr)

    func = getattr(module, func_name, None)

    if func is None:
        raise ValueError("Can't find function %s" % func_addr)

    if not inspect.isfunction(func):
        raise ValueError("%s is not a function" % func_addr)

    return func


def check_settings(psdash_settings):
    """
    :param psdash_settings: settings for psdash
    :type psdash_settings: dict
    :return: boolean
    """

    if not isinstance(psdash_settings, dict):
        raise ValueError('DJANGO_PSDASH_CATEGORIES should be dict')

    for key, value in psdash_settings.iteritems():

        if not isinstance(value, dict):
            raise ValueError(
                'Each item of DJANGO_PSDASH_CATEGORIES should be dict but'
                '%s is %s' % (key, type(value))
            )

        if not 'name' in value:
            raise ValueError(
                'Element "name" doesn\'t found in category %s' % key
            )

        if not 'panels' in value:
            raise ValueError(
                'Element "panels" doesn\'t found in category %s' % key
            )

        if not isinstance(value['panels'], Iterable):
            raise ValueError(
                'Element "panels" should be iterable not %s' % type(
                    value['panels']
                )
            )

