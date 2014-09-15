# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


def allow_logged(request):
    return request.user.is_authenticated


class MainViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.admin = User.objects.create_superuser(username='admin',
                                                   email='admin@admin.ru',
                                                   password='admin')
        self.user = User.objects.create_user(username='user',
                                             email='user@user.ru',
                                             password='user')

    def test_ok_access_for_admin(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('psdash_main'))
        self.assertEquals(response.status_code, 200)

    def test_forbidden_for_anonymous(self):
        response = self.client.get(reverse('psdash_main'))
        self.assertEquals(response.status_code, 403)

    def test_forbidden_for_logged_user(self):
        self.client.login(username='user', password='user')
        response = self.client.get(reverse('psdash_main'))
        self.assertEquals(response.status_code, 403)

    def test_allow_for_all_logged_users(self):
        setattr(
            settings,
            'PSDASH_PERMISSION_CHECKER',
            'tests.test_views.allow_logged'
        )

        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('psdash_main'))
        self.assertEquals(response.status_code, 200)
        self.client.logout()

        self.client.login(username='user', password='user')
        self.assertEquals(response.status_code, 200)
        self.client.logout()

        delattr(
            settings,
            'PSDASH_PERMISSION_CHECKER',
        )


class GetCategoriesTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        self.admin = User.objects.create_superuser(username='admin',
                                                   email='admin@admin.ru',
                                                   password='admin')

    def test_ok(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('psdash_categories'))
        self.assertEquals(response.status_code, 200)
