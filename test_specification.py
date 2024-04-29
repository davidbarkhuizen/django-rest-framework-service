import unittest
from unittest import TestCase

from entrypoint import server
from apis import CountriesAPI, CountryAPI

class UnitTests(TestCase):

    def test_get_countries_returns_a_list_of_country(self):
        with server.test_request_context(
            "/countries/", method="GET", json={},
        ):
            result, status_code = CountriesAPI().get()
            assert status_code == 200

            assert len(result.data) > 0
            # assert that elements in list are valid countries

    def test_get_countries_can_be_optionally_filtered_by_currency(self):
        with server.test_request_context(
            "/countries/", method="GET", query_string={
                "filter_field": "currency",
                "filter_value": "usd"
            }
        ):
            result, status_code = CountriesAPI().get()
            assert status_code == 200

            assert False


    def test_delete_countries(self):
        with server.test_request_context(
            "/countries/", method="DELETE", json={
                "ids": [], # us
            },
        ):
            result, status_code = CountriesAPI().delete()
            assert status_code == 200

            assert False

    def test_get_country_on_alpha_2_code(self):
        with server.test_request_context(
            "/country/", method="GET", query_string = {
                "filter_field": "alpha2",
                "filter_value": "za"
            }
        ):
            result, status_code = CountryAPI().get()
            assert status_code == 200

            assert False

    def test_get_country_on_alpha_3_code(self):
        with server.test_request_context(
            "/country/", method="GET", query_string={
                "filter_field": "alpha3",
                "filter_value": "zaf"
            },
        ):
            result, status_code = CountryAPI().get()
            assert status_code == 200

            assert False

if __name__ == "__main__":
    server.run()
    unittest.main()