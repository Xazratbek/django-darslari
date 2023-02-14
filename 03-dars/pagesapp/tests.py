from django.test import TestCase
from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)

    def test_our_projects_page_status_code(self):
        response = self.client.get('/our_projects/')
        self.assertEqual(response.status_code,200)

    def test_our_team_page_status_code(self):
        response = self.client.get('/our_team/')
        self.assertEqual(response.status_code,200)

    def interesting_facts_page_status_code(self):
        response = self.client.get('/facts/')
        self.assertEqual(reponse.status_code, 200)

#