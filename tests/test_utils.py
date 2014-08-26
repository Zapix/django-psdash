# -*- coding: utf-8 -*-
import inspect

from django import test

from django_psdash.utils import import_function


class ImportFunctionTestCase(test.TestCase):

    def raises_value_error(self, func_addr):
        with self.assertRaises(ValueError):
            import_function(func_addr)

    def test_wrong_addr(self):
        self.raises_value_error('')

        self.raises_value_error('.')

        self.raises_value_error('..')

        self.raises_value_error('.relative_path')

        self.raises_value_error('wrong_import.')

        self.raises_value_error('fake.module')

        self.raises_value_error('os')

        self.raises_value_error('os.wrong_function')

        self.raises_value_error('sys.args')

    def test_all_ok(self):

        func = import_function('os.path.join')

        self.assertTrue(inspect.isfunction(func))
