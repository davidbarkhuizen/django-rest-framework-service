from django.test import TestCase

class TestGetCountries(TestCase):
    
    def test_get_all_countries(self):
        response = self.client.get('/countries/')
        self.assertTrue(len(response.data) > 0)
