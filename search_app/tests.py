"""Tests for search_app"""

from django.test import TestCase
from django.urls import reverse


class Homepage(TestCase):
    """tests for homepage"""

    def test_homepage_connection(self):
        """status_code for connection to home page is 200"""
        response = self.client.get(reverse("search_app:home"))
        self.assertEqual(response.status_code, 200)

    def test_homepage_rendering(self):
        """Page displays "What do you want to search?" phrase"""
        response = self.client.get(reverse("search_app:home"))
        self.assertContains(response, "What do you want to search?")


class NewSearch(TestCase):
    """tests for new_search page"""

    def test_new_search_connection(self):
        """status_code for connection to new_search page is 200"""
        response = self.client.get(reverse("search_app:new_search"))
        self.assertEqual(response.status_code, 200)
