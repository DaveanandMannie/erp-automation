import unittest
import json
from pages import ShippingMethods
from time import sleep

class ShippingMethodTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shipping_method = ShippingMethods()
        cls.data: dict = cls._load_test_case_json()
        cls.shipping_method.login_staging()

    @classmethod
    def _load_test_case_json(cls):
        with open('test_json/allprefix.json', 'r') as file:
            return json.load(file)

    def setUp(self):
        self.shipping_method.navigate(self.data['staging_url'])
        self.shipping_method.navigate_tab_destination()
        sleep(0.2)

    def test_name(self):
        correct_name: str = self.data['shipping_method_name']
        name = self.shipping_method.get_name()
        self.assertEqual(name, correct_name, 'The name of the shipping method is incorrect')

    def test_provider(self):
        correct_provider: str = self.data['provider']
        provider = self.shipping_method.get_shipping_provider()
        self.assertEqual(provider, correct_provider, 'The "shipping provider" is inccorect')

    def test_related_company(self):
        correct_state: str = self.data['related_company_switch']
        state: str =  self.shipping_method.get_related_company()
        self.assertEqual(state, correct_state, 'Related to companies is not on')

    def test_company_names(self):
        correct_list: list = self.data['related_company_list']
        companies: list = self.shipping_method.get_company_names()
        self.assertEqual(companies, correct_list, 'The list of companies is not equal configured correctly')

    def test_countries(self):
        correct_countries: list = self.data['country_list']
        countries: list = self.shipping_method.get_countries()
        self.assertEqual(countries, correct_countries, 'The list of countries is not configured correctly')

    def test_states(self):
        correct_states: list = self.data['state_list']
        states: list = self.shipping_method.get_states()
        self.assertEqual(states, correct_states, 'The list of states is not configured correctly')

    def test_zip_prefix(self):
        correct_prefix: list = self.data['zip_prefix_list']
        prefix: list = self.shipping_method.get_zip_prefix()
        self.assertEqual(prefix, correct_prefix, 'The zip prefrix is not configured correctly')


    def test_default_weight(self):
        self.shipping_method.navigate_tab_extra()
        correct_default = self.data['default_weight']
        default = self.shipping_method.get_default_weight()
        self.assertEqual(default, correct_default)

if __name__ == '__main__':
    unittest.main()

