import pytest
import json
from pages import ShippingMethods
from time import sleep
from glob import glob

# TODO: change sleep here to EC driver wait in the class ShippingMethods
class TestShippingMethods:
    @pytest.fixture(scope="class")
    def page(self):
        ''' Selenium driver with scraper '''
        page: ShippingMethods = ShippingMethods('--kiosk', 'window-size=1200x600')
        page.login_staging()
        return page
    # TODO: dynamically add staging vs prod bool
    @pytest.fixture(params=glob('testcase_json/*.json'))
    def data(self, request, page: ShippingMethods):
        ''' Paramitize for multiple json test cases '''
        with open(request.param, 'r') as file:
            data = json.load(file)
            page.navigate(data['staging_url'])
            sleep(0.5)
            return data


    def test_name(self, page: ShippingMethods, data: dict):
        page.navigate_tab_destination()
        sleep(0.1)
        correct_name: str = data['shipping_method_name']
        name = page.get_name()
        assert name == correct_name, 'The name of the shipping method is incorrect'

    def test_provider(self, page: ShippingMethods, data: dict):
        page.navigate_tab_destination()
        sleep(0.1)
        correct_provider: str = data['provider']
        provider = page.get_shipping_provider()
        assert provider == correct_provider, 'The shipping provider is incorrect'


    def test_related_company(self, page: ShippingMethods, data: dict):
        page.navigate_tab_destination()
        sleep(0.1)
        correct_state: str = data['related_company_switch']
        state: str = page.get_related_company()
        assert state == correct_state, 'Related to companies is not on'


    def test_company_names(self, page: ShippingMethods, data: dict):
        page.navigate_tab_destination()
        sleep(0.1)
        correct_list: list = data['related_company_list']
        companies: list = page.get_company_names()
        assert companies == correct_list, 'The list of companies is not equal configured correctly'

    def test_countries(self, page: ShippingMethods, data: dict):
        page.navigate_tab_destination()
        correct_countries: list = data['country_list']
        sleep(0.1)
        countries: list = page.get_countries()
        assert countries ==  correct_countries, 'The list of countries is not configured correctly'

    def test_states(self, page: ShippingMethods, data: dict):
        page.navigate_tab_destination()
        sleep(0.1)
        correct_states: list = data['state_list']
        states: list = page.get_states()
        assert states == correct_states, 'The list of states is not configured correctly'

    def test_zip_prefix(self, page: ShippingMethods, data: dict):
        page.navigate_tab_destination()
        sleep(0.1)
        correct_prefix: list = data['zip_prefix_list']
        prefix: list = page.get_zip_prefix()
        assert prefix == correct_prefix, 'The zip prefix is not configured correctly'

    # ==================Extra Tab================== #
    def test_default_weight(self, page: ShippingMethods, data: dict):
        page.navigate_tab_extra()
        sleep(0.1)
        correct_default: str = data['default_weight']
        default: str = page.get_default_weight()
        assert default ==  correct_default, 'the default weight is not configured correctly'

    def test_shipping_uom(self, page: ShippingMethods, data: dict):
        page.navigate_tab_extra()
        sleep(0.1)
        correct_uom: str = data['shipping_uom']
        uom: str = page.get_shipping_uom()
        assert uom == correct_uom, 'The shipping unit of measure is not configured correctly'

    def test_packaging(self, page: ShippingMethods, data: dict):
        page.navigate_tab_extra()
        sleep(0.1)
        correct_package: str = data['packaging']
        package: str = page.get_packaging()
        assert package == correct_package, ' The packaging is not configured correctly'

    def test_void_ship(self, page: ShippingMethods, data: dict):
        page.navigate_tab_extra()
        sleep(0.1)
        correct_state: str = data['void_shipment_switch']
        state: str = page.get_void_ship()
        assert state == correct_state, 'Void shipment is not on'

    def test_service_type(self, page: ShippingMethods, data: dict):
        page.navigate_tab_extra()
        sleep(0.1)
        correct_service: str = data['service_type']
        service: str = page.get_service_type()
        assert service == correct_service, 'Service type was not configured correctly'

    def test_service_option(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:
            assert True
            return
        page.navigate_tab_extra()
        sleep(0.1)
        correct_option: str = data['desired_option']
        option: str = page.get_service_option()
        assert option == correct_option, 'Option type was not configured correctly'

    def test_customer_type(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:
            assert True
            return
        page.navigate_tab_extra()
        sleep(0.1)
        correct_type: str = data['customer_type']
        c_type: str = page.get_customer_type()
        assert c_type == correct_type, 'Customer type is not configured correctly'

    def test_customer_num(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:
            assert True
            return
        page.navigate_tab_extra()
        sleep(0.1)
        correct_num: str = data['customer_number']
        num: str = page.get_customer_number()
        assert num == correct_num, 'Customer number is not configured correctly'

    def test_contract_id(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:
            assert True
            return
        page.navigate_tab_extra()
        sleep(0.1)
        correct_contract: str = data['contract_id']
        contract: str = page.get_contract_id()
        assert contract == correct_contract, 'Contract number is not configured correctly'

    def test_promo(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:
            assert True
            return
        page.navigate_tab_extra()
        sleep(0.1)
        correct_promo: str = data['promo_code']
        promo: str = page.get_promo_code()
        assert promo == correct_promo, 'Promo code is not configured correctly'

    def test_payment_method(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:
            assert True
            return
        page.navigate_tab_extra()
        sleep(0.1)
        correct_method: str = data['method_of_payments']
        method: str = page.get_payment_method()
        assert method ==  correct_method, 'Method of payment is not configured correctly'

    def test_on_behalf(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:
            assert True
            return
        page.navigate_tab_extra()
        sleep(0.1)
        correct_behalf: str = data['on_behalf_of']
        behalf: str = page.get_mailed_on_behalf()
        assert behalf == correct_behalf, 'Mailed on behalf of is not configured correctly'

    # ==================Product Attrib Tab================== #
    def test_included_attrib(self, page: ShippingMethods, data: dict):
        page.navigate_tab_product_attrib()
        sleep(0.1)
        correct_include: list = data['included_attributes']
        include: list = page.get_included_attribs()
        assert include == correct_include, 'Included attributes are not configured correctly'

    def test_excluded_attrib(self, page: ShippingMethods, data: dict):
        sleep(0.1)
        page.navigate_tab_product_attrib()
        correct_exclude: list = data['included_attributes']
        exclude: list = page.get_included_attribs()
        assert exclude == correct_exclude, 'Excluded attributes are not configured correctly'
