# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class MainViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_view(self):
        response = self.client.get(reverse('psdash_main'))
        self.assertEquals(response.status_code, 200)
