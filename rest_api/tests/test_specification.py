from django.test import TestCase
from marshmallow import Schema, fields

class CountrySchema(Schema):
    name = fields.Str(required=True)
    alpha2 = fields.Str(required=True)
    alpha3 = fields.Str(required=True)   
    currencies = fields.List(fields.String(), required=True)

PATH_ROOT = '/countries/'

class TestOverallServiceSpecification(TestCase):

    def test_it_can_list_all_countries_providing_at_least_country_name_alpha2_alpha_and_currencies(self):
        
        response = self.client.get(PATH_ROOT)

        self.assertTrue(len(response.data) > 0)

        country_validator = CountrySchema()
        self.assertTrue(sum (x for x in response.data if not country_validator.validate(x)) == 0)
        
    def test_that_list_all_currencies_can_be_filtered_by_currency(self):

        alpha3 = 'gbp'
        url = f'{PATH_ROOT}?currencies__alpha3={alpha3}'
        response = self.client.get(url)

        self.assertTrue(len(response.data) == 1)
        self.assertTrue(alpha3 in response.data[0]['currencies'])

    def test_that_get_single_country_based_upon_alpha2(self):
        alpha2 = 'za'
        url = f'{PATH_ROOT}{alpha2}/'
        response = self.client.get(url)
        self.assertTrue(alpha2 == response.data['alpha2'])

    def test_that_get_single_country_based_upon_alpha3(self):
        alpha3 = 'zaf'
        url = f'{PATH_ROOT}{alpha3}/'
        response = self.client.get(url)
        self.assertTrue(alpha3 == response.data['alpha3'])

    def test_the_interface_allowing_soft_deletion_of_countries(self):

        alpha2 = 'za'
        get_url = f'{PATH_ROOT}{alpha2}/'

        response = self.client.get(get_url)
        self.assertTrue(response.status_code == 200)

        id = response.data['id']
        delete_url = f'{PATH_ROOT}{id}/'

        response = self.client.delete(delete_url)
        self.assertTrue(response.status_code == 204)

        response = self.client.get(get_url)
        self.assertTrue(response.data['deleted_date'] is not None)
