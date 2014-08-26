# -*- coding: utf-8 -*-
import inspect

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



