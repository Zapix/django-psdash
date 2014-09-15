# -*- coding: utf-8 -*-
import inspect

from django import test

from django_psdash.utils import import_function
from django_psdash.utils import check_settings


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


class CheckCategoriesSettingsTestCase(test.TestCase):

    def test_wrong_type(self):
        with self.assertRaises(ValueError):
            check_settings([1, 2, 3])

    def test_wrong_item_of_categories(self):
        with self.assertRaises(ValueError):
            check_settings({'test': []})

    def test_required_name_for_item(self):
        with self.assertRaises(ValueError):
            check_settings(
                {
                    'test': {
                        'panels': []
                    }
                }
            )

    def test_required_panels_for_item(self):
        with self.assertRaises(ValueError):
            check_settings(
                {
                    'test': {
                        'name': 'Test',
                    }
                }
            )

    def test_panels_should_be_a_list(self):
        with self.assertRaises(ValueError):
            check_settings({
                'test': {
                    'name': 'Test',
                    'panels': 1
                }
            })
