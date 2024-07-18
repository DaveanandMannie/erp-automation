import unittest
import json
from pages import ShippingMethods

class ShippingMethodTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shipping_method = ShippingMethods()
        cls.data: dict = cls._load_test_case_json()
        cls.shipping_method.login_staging()

    def setUp(self):
        self.shipping_method.navigate(self.data['staging_url'])

    @classmethod
    def _load_test_case_json(cls):
        with open('test_json/allprefix.json', 'r') as file:
            return json.load(file)

    def test_name(self):
        correct_name: str = self.data['shipping_method_name']
        name = self.shipping_method.get_name()
        self.assertEqual(name, correct_name, 'The name of the shipping method is incorrect')

    def test_provider(self):
        correct_provider: str = self.data['provider']
        provider = self.shipping_method.get_shipping_provider()
        self.assertEqual(provider, correct_provider, 'The "shipping provider" is inccorect')

if __name__ == '__main__':
    unittest.main()

