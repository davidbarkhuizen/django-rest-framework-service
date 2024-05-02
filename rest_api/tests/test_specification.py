from django.test import TestCase
from marshmallow import Schema, fields

class CountrySchema(Schema):
    name = fields.Str(required=True)
    alpha2 = fields.Str(required=True)
    alpha3 = fields.Str(required=True)   
    currencies = fields.List(fields.String(), required=True)

class TestOverallServiceSpecification(TestCase):

    def test_it_can_list_all_countries_providing_at_least_country_name_alpha2_alpha_and_currencies(self):
        response = self.client.get('/countries/')

        validator = CountrySchema()

        self.assertTrue(len(response.data) > 0)

        self.assertTrue(sum (x for x in response.data if not validator.validate(x)) == 0)
        
