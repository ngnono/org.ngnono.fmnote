"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from apps.bill.forms import BillForm


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class BillTest(TestCase):
    def setUp(self, *args, **kwargs):
        self.bill = {
            "title": "1",

        }

        f = BillForm(self.bill)
        f.save()
        self.bill["title"] = "my new title"

    def test_properties_cannot_empty(self):
        f = BillForm({})
        self.assertFalse(f.is_valid())
        self.assertTrue(f["title"].errors)
