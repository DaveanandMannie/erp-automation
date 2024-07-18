import unittest
import json
from pages import ShippingMethods

class ShippingMethodtTest(unittest.TestCase):
    def setUp(self):
        self.shipping_method = ShippingMethods()
        self.data: dict = self._load_test_case_json()
        self.shipping_method.login_staging()
        self.shipping_method.navigate(self.data['staging_url'])
    
    def _load_test_case_json(self):
        with open('test_json/allprefix.json', 'r') as file:
            return json.load(file)

    def test_name(self):
        correct_name: str = self.data['shipping_method_name']
        name = self.shipping_method.get_name()
        self.assertEqual(name, correct_name, 'The name of the shipping method is incorrect')

if __name__ == '__main__':
    unittest.main()

