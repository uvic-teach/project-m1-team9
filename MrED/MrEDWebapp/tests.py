"""Test suite for Mr. ED"""
from django.test import TestCase, Client

class ViewsTestCase(TestCase):
    """Test cases for view classes"""
    client = None

    def setUp(self):
        self.client = Client()

    def test_home(self):
        """Tests GET and template for home view page"""
        response = self.client.get("/mred/", follow=True)
        self.assertTemplateUsed(response, "home.html")
        self.assertEqual(response.status_code, 200)