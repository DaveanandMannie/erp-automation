import unittest
import json
from pages import ShippingMethods
from time import sleep


class ShippingMethodTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = ShippingMethods()
        cls.data: dict = cls._load_test_case_json()
        cls.page.login_staging()

    @classmethod
    def _load_test_case_json(cls):
        with open('testcase_json/allprefix.json', 'r') as file:
            return json.load(file)

    def setUp(self):
        self.page.navigate(self.data['staging_url'])
        self.page.navigate_tab_destination()
        sleep(0.2)

    def test_name(self):
        correct_name: str = self.data['shipping_method_name']
        name = self.page.get_name()
        self.assertEqual(name, correct_name, 'The name of the shipping method is incorrect')

    def test_provider(self):
        correct_provider: str = self.data['provider']
        provider = self.page.get_shipping_provider()
        self.assertEqual(provider, correct_provider, 'The "shipping provider" is incorrect')

    def test_related_company(self):
        correct_state: str = self.data['related_company_switch']
        state: str = self.page.get_related_company()
        self.assertEqual(state, correct_state, 'Related to companies is not on')

    def test_company_names(self):
        correct_list: list = self.data['related_company_list']
        companies: list = self.page.get_company_names()
        self.assertEqual(companies, correct_list, 'The list of companies is not equal configured correctly')

    def test_countries(self):
        correct_countries: list = self.data['country_list']
        countries: list = self.page.get_countries()
        self.assertEqual(countries, correct_countries, 'The list of countries is not configured correctly')

    def test_states(self):
        correct_states: list = self.data['state_list']
        states: list = self.page.get_states()
        self.assertEqual(states, correct_states, 'The list of states is not configured correctly')

    def test_zip_prefix(self):
        correct_prefix: list = self.data['zip_prefix_list']
        prefix: list = self.page.get_zip_prefix()
        self.assertEqual(prefix, correct_prefix, 'The zip prefix is not configured correctly')

    def test_default_weight(self):
        self.page.navigate_tab_extra()
        correct_default: str = self.data['default_weight']
        default: str = self.page.get_default_weight()
        self.assertEqual(default, correct_default, 'the default weight is not configured correctly')

    def test_shipping_uom(self):
        self.page.navigate_tab_extra()
        correct_uom: str = self.data['shipping_uom']
        uom: str = self.page.get_shipping_uom()
        self.assertEqual(uom, correct_uom, 'The shipping unit of measure is not configured correctly')

    def test_packaging(self):
        self.page.navigate_tab_extra()
        correct_package: str = self.data['packaging']
        package: str = self.page.get_packaging()
        self.assertEqual(package, correct_package, ' The packaging is not configured correctly')

    def test_void_ship(self):
        self.page.navigate_tab_extra()
        correct_state: str = self.data['void_shipment_switch']
        state: str = self.page.get_void_ship()
        self.assertEqual(state, correct_state, 'Void shipment is not on')

    def test_service_type(self):
        self.page.navigate_tab_extra()
        correct_service: str = self.data['service_type']
        service: str = self.page.get_service_type()
        self.assertEqual(service, correct_service, 'Service type was not configured correctly')

    def test_service_option(self):
        self.page.navigate_tab_extra()
        correct_option: str = self.data['desired_option']
        option: str = self.page.get_service_option()
        self.assertEqual(option, correct_option, 'Option type was not configured correctly')

    def test_customer_type(self):
        self.page.navigate_tab_extra()
        correct_type: str = self.data['customer_type']
        c_type: str = self.page.get_customer_type()
        self.assertEqual(c_type, correct_type, 'Customer type is not configured correctly')

    def test_customer_num(self):
        self.page.navigate_tab_extra()
        correct_num: str = self.data['customer_number']
        num: str = self.page.get_customer_number()
        self.assertEqual(num, correct_num, 'Customer number is not configured correctly')

    def test_contract_id(self):
        self.page.navigate_tab_extra()
        correct_contract: str = self.data['contract_id']
        contract: str = self.page.get_contract_id()
        self.assertEqual(contract, correct_contract, 'Contract number is not configured correctly')

    def test_promo(self):
        self.page.navigate_tab_extra()
        correct_promo: str = self.data['promo_code']
        promo: str = self.page.get_promo_code()
        self.assertEqual(promo, correct_promo, 'Promo code is not configured correctly')

    def test_payment_method(self):
        self.page.navigate_tab_extra()
        correct_method: str = self.data['method_of_payments']
        method: str = self.page.get_payment_method()
        self.assertEqual(method, correct_method, 'Method of payment is not configured correctly')

    def test_on_behalf(self):
        self.page.navigate_tab_extra()
        correct_behalf: str = self.data['on_behalf_of']
        behalf: str = self.page.get_mailed_on_behalf()
        self.assertEqual(behalf, correct_behalf, 'Mailed on behalf of is not configured correctly')


if __name__ == '__main__':
    unittest.main()
