import pytest
import json
from pages.shipping_methods import ShippingMethods
from time import sleep
from glob import glob


# TODO: add dynamic test name to failure message
class TestShippingMethods:
    @pytest.fixture(scope='class')
    def page(self, request):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')
        page: ShippingMethods = ShippingMethods("--headless")
        if environment == 'staging':
            page.login_staging()
        if environment == 'production':
            page.login_prod()
        return page

    @pytest.fixture(
        scope='class',
        params=glob('testcases_json/shipping_methods/*.json')
    )
    def data(self, request, page: ShippingMethods, environment: str):
        """ Paramitize for multiple json test cases """
        with open(request.param, 'r') as file:
            data = json.load(file)
            if environment == 'staging':
                page.navigate(data['staging_url'])

            if environment == 'production':
                page.navigate(data['production_url'])

            sleep(0.5)
            return data

    def test_name(self, page: ShippingMethods, data: dict):
        page.navigate_tab_destination()
        correct_name: str = data['shipping_method_name']
        name = page.get_name()
        assert name == correct_name, (
                'The name of the shipping method is incorrect'
        )

    def test_provider(self, page: ShippingMethods, data: dict):
        page.navigate_tab_destination()
        correct_provider: str = data['provider']
        provider = page.get_shipping_provider()

        if 'Letter Mail' in data['shipping_method_name']:
            provider = provider.replace('_', ' ').title()
        assert provider == correct_provider, (
                'The shipping provider is incorrect'
        )

    def test_related_company(self, page: ShippingMethods, data: dict):
        page.navigate_tab_destination()
        correct_state: bool = bool(data['related_company_switch'])
        state: bool = page.get_related_company()
        assert state == correct_state, 'Related to companies is not on'

    def test_company_names(self, page: ShippingMethods, data: dict):
        page.navigate_tab_destination()
        correct_list: list = data['related_company_list']
        companies: list = page.get_company_names()
        assert companies == correct_list, (
            'The list of companies is not equal configured correctly'
        )

    def test_delivery_product(self, page: ShippingMethods, data: dict):
        correct_product: str = data['delivery_product']
        product: str = page.get_delivery_product()
        assert product == correct_product, (
            'Delivery Product is not configured correctly'
        )

    def test_countries(self, page: ShippingMethods, data: dict):
        page.navigate_tab_destination()
        correct_countries: list = data['country_list']
        countries: list = page.get_countries()
        assert countries == correct_countries, (
                'The list of countries is not configured correctly'
        )

    def test_states(self, page: ShippingMethods, data: dict):
        page.navigate_tab_destination()
        correct_states: list = data['state_list']
        states: list = page.get_states()
        assert states == correct_states, (
                'The list of states is not configured correctly'
        )

    def test_zip_prefix(self, page: ShippingMethods, data: dict):
        page.navigate_tab_destination()
        correct_prefix: list = data['zip_prefix_list']
        prefix: list = page.get_zip_prefix()
        assert prefix == correct_prefix, (
                'The zip prefix is not configured correctly'
        )

    # ==================Extra Tab================== #
    def test_default_weight(self, page: ShippingMethods, data: dict):
        page.navigate_tab_extra()
        correct_default: str = data['default_weight']
        default: str = page.get_default_weight()
        assert default == correct_default, (
                'the default weight is not configured correctly'
        )

    def test_shipping_uom(self, page: ShippingMethods, data: dict):
        page.navigate_tab_extra()
        correct_uom: str = data['shipping_uom']
        uom: str = page.get_shipping_uom()
        assert uom == correct_uom, (
                'The shipping unit of measure is not configured correctly'
        )

    def test_packaging(self, page: ShippingMethods, data: dict):
        page.navigate_tab_extra()
        correct_package: str = data['packaging']
        package: str = page.get_packaging()
        assert package == correct_package, (
                'The packaging is not configured correctly'
        )

    def test_void_ship(self, page: ShippingMethods, data: dict):
        page.navigate_tab_extra()
        correct_state: bool = bool(data['void_shipment_switch'])
        state: bool = page.get_void_ship()
        assert state == correct_state, 'Void shipment is not on'

    def test_service_type(self, page: ShippingMethods, data: dict, environment: str):  # noqa: E501
        if environment == 'production':
            # TODO: REMOVE ONCE PROD IS UPDATED
            pytest.skip('REMOVE ONCE PROD IS UPGRADED')

        correct_service: str = data['service_type']
        service: str = page.get_service_type()
        assert service == correct_service, (
                'Service type was not configured correctly'
        )

    def test_service_option(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:
            pytest.skip(f'Skipping Canada Post specific test on {data['shipping_method_name']}')  # noqa: E501

        if 'Letter Mail' in data['shipping_method_name']:
            pytest.skip(f'Skipping APPAREL specific test on {data['shipping_method_name']}')  # noqa: E501

        page.navigate_tab_extra()
        correct_option: str = data['desired_option']
        option: str = page.get_service_option()
        assert option == correct_option, (
                'Option type was not configured correctly'
        )

    def test_customer_type(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:
            pytest.skip(f'Skipping Canada Post specific test on {data['shipping_method_name']}')  # noqa: E501

        if 'Letter Mail' in data['shipping_method_name']:
            pytest.skip(f'Skipping APPAREL specific test on {data['shipping_method_name']}')  # noqa: E501

        page.navigate_tab_extra()
        correct_type: str = data['customer_type']
        c_type: str = page.get_customer_type()
        assert c_type == correct_type, (
                'Customer type is not configured correctly'
        )

    def test_customer_num(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:
            pytest.skip(f'Skipping Canada Post specific test on {data['shipping_method_name']}')  # noqa: E501

        if 'Letter Mail' in data['shipping_method_name']:
            pytest.skip(f'Skipping APPAREL specific test on {data['shipping_method_name']}')  # noqa: E501

        page.navigate_tab_extra()
        correct_num: str = data['customer_number']
        num: str = page.get_customer_number()
        assert num == correct_num, (
                'Customer number is not configured correctly'
        )

    def test_contract_id(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:
            pytest.skip(f'Skipping Canada Post specific test on {data['shipping_method_name']}')  # noqa: E501

        if 'Letter Mail' in data['shipping_method_name']:
            pytest.skip(f'Skipping APPAREL specific test on {data['shipping_method_name']}')  # noqa: E501

        page.navigate_tab_extra()
        correct_contract: str = data['contract_id']
        contract: str = page.get_contract_id()
        assert contract == correct_contract, (
                'Contract number is not configured correctly'
        )

    def test_promo(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:
            pytest.skip(f'Skipping Canada Post specific test on {data['shipping_method_name']}')  # noqa: E501

        if 'Letter Mail' in data['shipping_method_name']:
            pytest.skip(f'Skipping APPAREL specific test on {data['shipping_method_name']}')  # noqa: E501

        page.navigate_tab_extra()
        correct_promo: str = data['promo_code']
        promo: str = page.get_promo_code()
        assert promo == correct_promo, 'Promo code is not configured correctly'

    def test_payment_method(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:
            pytest.skip(f'Skipping Canada Post specific test on {data['shipping_method_name']}')  # noqa: E501

        if 'Letter Mail' in data['shipping_method_name']:
            pytest.skip(f'Skipping APPAREL specific test on {data['shipping_method_name']}')  # noqa: E501

        page.navigate_tab_extra()
        correct_method: str = data['method_of_payments']
        method: str = page.get_payment_method()
        assert method == correct_method, (
                'Method of payment is not configured correctly'
        )

    def test_on_behalf(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:
            pytest.skip(f'Skipping Canada Post specific test on {data['shipping_method_name']}')  # noqa: E501

        if 'Letter Mail' in data['shipping_method_name']:
            pytest.skip(f'Skipping APPAREL specific test on {data['shipping_method_name']}')  # noqa: E501
        page.navigate_tab_extra()
        correct_behalf: str = data['on_behalf_of']
        behalf: str = page.get_mailed_on_behalf()
        assert behalf == correct_behalf, (
                'Mailed on behalf of is not configured correctly'
        )

    # ==================Credential Tab(s)================== #
    def test_canpost_tests_user(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:  # noqa: E501
            pytest.skip(f'Skipping Canada Post specific test on {data['shipping_method_name']}')  # noqa: E501

        if 'Letter Mail' in data['shipping_method_name']:
            pytest.skip(f'Skipping APPAREL specific test on {data['shipping_method_name']}')  # noqa: E501

        page.navigate_tab_canpost_credentials()
        correct_user: str = data['test_username']
        user: str = page.get_canpost_dev_username()
        assert user == correct_user, (
            'Canada Post staging username is not configured correctly'
        )

    def test_canpost_tests_pass(self, page: ShippingMethods, data: dict):
        if 'Pitney' in data['shipping_method_name']:
            pytest.skip(f'Skipping Canada Post specific test on {data['shipping_method_name']}')  # noqa: E501

        if 'Letter Mail' in data['shipping_method_name']:
            pytest.skip(f'Skipping APPAREL specific test on {data['shipping_method_name']}')  # noqa: E501

        page.navigate_tab_canpost_credentials()
        correct_pass: str = data['test_password']
        password: str = page.get_canpost_dev_password()
        assert password == correct_pass, (
            'Canada Post staging password is not configured correctly'
        )

    def test_canpost_prod_user(self, page: ShippingMethods, data: dict, environment: str):  # noqa: E501
        if 'Pitney' in data['shipping_method_name']:
            pytest.skip(f'Skipping Canada Post specific test on {data['shipping_method_name']}')  # noqa: E501

        if 'Letter Mail' in data['shipping_method_name']:
            pytest.skip(f'Skipping APPAREL specific test on {data['shipping_method_name']}')  # noqa: E501

        if environment == 'staging':
            pytest.skip('Skipping production credential check')

        page.navigate_tab_canpost_credentials()
        correct_user: str = data['production_username']
        user: str = page.get_canpost_prod_username()
        assert user == correct_user, (
            'Canada Post production username is not configured correctly'
        )

    def test_canpost_prod_pass(self, page: ShippingMethods, data: dict, environment: str):  # noqa: E501
        if 'Pitney' in data['shipping_method_name']:
            pytest.skip(f'Skipping Canada Post specific test on {data['shipping_method_name']}')  # noqa: E501

        if 'Letter Mail' in data['shipping_method_name']:
            pytest.skip(f'Skipping APPAREL specific test on {data['shipping_method_name']}')  # noqa: E501

        if environment == 'staging':
            pytest.skip('Skipping production credential check')

        page.navigate_tab_canpost_credentials()
        correct_pass: str = data['production_password']
        password: str = page.get_canpost_prod_password()
        assert password == correct_pass, (
            'Canada Post production password is not configured correctly'
        )

    # ==================Product Attrib Tab================== #
    def test_included_attrib(self, page: ShippingMethods, data: dict, environment: str):  # noqa: E501
        if environment == 'production' and 'Letter Mail' in data['shipping_method_name']:  # noqa: E501
            # TODO: REMOVE ONCE PROD IS UPDATED
            pytest.skip('REMOVE ONCE PROD IS UPGRADED')

        page.navigate_tab_product_attrib()
        correct_include: list = data['included_attributes']
        include: list = page.get_included_attribs()
        assert include == correct_include, (
                'Included attributes are not configured correctly'
        )

    def test_excluded_attrib(self, page: ShippingMethods, data: dict, environment: str):  # noqa: E501
        if environment == 'production' and 'Letter Mail' in data['shipping_method_name']:  # noqa: E501
            # TODO: REMOVE ONCE PROD IS UPDATED
            pytest.skip('REMOVE ONCE PROD IS UPGRADED')

        page.navigate_tab_product_attrib()
        correct_exclude: list = data['included_attributes']
        exclude: list = page.get_included_attribs()
        assert exclude == correct_exclude, (
                'Excluded attributes are not configured correctly'
        )
