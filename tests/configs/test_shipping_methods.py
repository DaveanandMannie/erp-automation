import json
from glob import glob
from time import sleep
from typing import Any, cast

import pytest
from pages.configs.shipping_methods import ShippingMethods
from pytest import FixtureRequest


class TestParcel:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        page: ShippingMethods
        if driver_arg:
            page = ShippingMethods(driver_arg)
        else:
            page = ShippingMethods()

        if environment == 'staging':
            page.login_staging()

        if environment == 'production':
            page.login_prod()

        if environment == 'uat':
            page.login_uat()

        return page

    @pytest.fixture(
        scope='class',
        params=glob(
            'testcases_json/configs/shipping_methods/canada_post/parcel/*.json'
        )
    )
    def data(self,
             request: FixtureRequest,
             page: ShippingMethods,
             environment: str
             ) -> dict[str, Any]:
        """ Paramitize for multiple json test cases """
        fp: str = cast(str, request.param)
        with open(fp) as file:
            data: dict[str, Any] = json.load(file)
            if environment == 'staging':
                page.navigate(cast(str, data['staging_url']))

            if environment == 'production':
                page.navigate(cast(str, data['production_url']))

            if environment == 'uat':
                page.navigate(cast(str, data['uat_url']))

            sleep(0.5)
            return data

    # ============= Tests ============= #

    def test_name(self, page: ShippingMethods, data: dict[str, Any]):
        sleep(0.2)
        correct_name: str = data['shipping_method_name']
        name = page.get_name()
        assert name == correct_name, (
                'The name of the shipping method is incorrect'
        )

    def test_provider(self, page: ShippingMethods, data: dict[str, Any]):
        correct_provider: str = data['provider']
        provider = page.get_shipping_provider()

        assert provider == correct_provider, (
                'The shipping provider is incorrect'
        )

    def test_routes(self, page: ShippingMethods, data: dict[str, Any]):
        correct_routes: str = data['routes']
        routes: str | None = page.get_routes()
        assert routes == correct_routes, 'The routes is incorrect'

    def test_margin_rate(self, page: ShippingMethods, data: dict[str, Any]):
        correct_rate: str = data['margin']
        rate: str | None = page.get_margin()
        assert rate == correct_rate, 'The Margin on Rate is incorrect'

    def test_add_margin(self, page: ShippingMethods, data: dict[str, Any]):
        correct_add: str = data['additional_margin']
        add: str | None = page.get_add_margin()
        assert add == correct_add, 'Additional Margin is incorrect'

    def test_delivery_product(self,
                              page: ShippingMethods,
                              data: dict[str, Any]
                              ):
        correct_product: str = data['delivery_product']
        product: str | None = page.get_delivery_product()
        assert product == correct_product, (
            'Delivery Product is not configured correctly'
        )

    def test_invoicing_policy(self,
                              page: ShippingMethods,
                              data: dict[str, Any]
                              ):
        correct_val: str = data['invoice_policy']
        val: str | None = page.get_invoice_policy()
        assert val == correct_val, 'Invoicing policy is inccoret'

    def test_related_company(self,
                             page: ShippingMethods,
                             data: dict[str, Any]
                             ):
        page.navigate_tab_destination()
        correct_state: str = data['related_company_switch']
        state: str = str(page.get_related_company())
        assert state == correct_state, 'Related to companies is not on'

        if correct_state:
            correct_list: list[str] = data['related_company_list']
            companies: list[str] = page.opt_company_names()
            assert companies == correct_list, (
                'The list of companies is not equal configured correctly'
            )

    # =============== Destination Availability=============== #

    def test_countries(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_destination()
        correct_countries: list[str] = data['country_list']
        countries: list[str] = page.get_countries()
        assert countries == correct_countries, (
                'The list of countries is not configured correctly'
        )

    def test_states(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_destination()
        correct_states: list[str] = data['state_list']
        states: list[str] = page.get_states()
        assert states == correct_states, (
                'The list of states is not configured correctly'
        )

    def test_zip_prefix(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_destination()
        correct_prefix: list[str] = data['zip_prefix_list']
        prefix: list[str] = page.get_zip_prefix()
        assert prefix == correct_prefix, (
                'The zip prefix is not configured correctly'
        )

    # ==================Extra Tab================== #
    def test_default_weight(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_extra()
        correct_default: str = data['default_weight']
        default: str | None = page.get_default_weight()
        assert default == correct_default, (
                'the default weight is not configured correctly'
        )

    def test_shipping_uom(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_extra()
        correct_uom: str = data['shipping_uom']
        uom: str | None = page.get_shipping_uom()
        assert uom == correct_uom, (
                'The shipping unit of measure is not configured correctly'
        )

    def test_packaging(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_extra()
        correct_package: str = data['packaging']
        package: str | None = page.get_packaging()
        assert package == correct_package, (
                'The packaging is not configured correctly'
        )

    def test_void_ship(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_extra()
        correct_state: str = data['void_shipment_switch']
        state: str = str(page.get_void_ship())
        assert state == correct_state, 'Void shipment is not on'

    def test_service_type(self, page: ShippingMethods, data: dict[str, Any]):
        correct_service: str = data['service_type']
        service: str | None = page.get_service_type()
        assert service == correct_service, (
                'Service type was not configured correctly'
        )

    def test_service_option(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_extra()
        correct_option: str = data['desired_option']
        option: str | None = page.get_service_option()
        assert option == correct_option, (
                'Option type was not configured correctly'
        )

    def test_customer_type(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_extra()
        correct_type: str = data['customer_type']
        c_type: str = page.get_customer_type()
        assert c_type == correct_type, (
                'Customer type is not configured correctly'
        )

    def test_customer_num(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_extra()
        correct_num: str = data['customer_number']
        num: str | None = page.get_customer_number()
        assert num == correct_num, (
                'Customer number is not configured correctly'
        )

    def test_contract_id(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_extra()
        correct_contract: str = data['contract_id']
        contract: str | None = page.get_contract_id()
        assert contract == correct_contract, (
                'Contract number is not configured correctly'
        )

    def test_promo(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_extra()
        correct_promo: str = data['promo_code']
        promo: str | None = page.get_promo_code()
        assert promo == correct_promo, 'Promo code is not configured correctly'

    def test_payment_method(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_extra()
        correct_method: str = data['method_of_payments']
        method: str | None = page.get_payment_method()
        assert method == correct_method, (
                'Method of payment is not configured correctly'
        )

    def test_on_behalf(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_extra()
        correct_behalf: str = data['on_behalf_of']
        behalf: str | None = page.get_mailed_on_behalf()
        assert behalf == correct_behalf, (
                'Mailed on behalf of is not configured correctly'
        )

    # ==================Credential Tab(s)================== #
    def test_canpost_tests_user(self,
                                page: ShippingMethods,
                                data: dict[str, Any]
                                ):
        page.navigate_tab_credentials()
        correct_user: str = data['test_username']
        user: str | None = page.get_dev_username()
        assert user == correct_user, (
            'Canada Post staging username is not configured correctly'
        )

    def test_canpost_tests_pass(self,
                                page: ShippingMethods,
                                data: dict[str, Any]
                                ):
        page.navigate_tab_credentials()
        correct_pass: str = data['test_password']
        password: str | None = page.get_dev_password()
        assert password == correct_pass, (
            'Canada Post staging password is not configured correctly'
        )

    def test_canpost_prod_user(self,
                               page: ShippingMethods,
                               data: dict[str, Any]
                               ):
        correct_user: str = data['production_username']
        user: str | None = page.get_prod_username()
        assert user == correct_user, (
            'Canada Post production username is not configured correctly'
        )

    def test_canpost_prod_pass(self,
                               page: ShippingMethods,
                               data: dict[str, Any]
                               ):
        page.navigate_tab_credentials()
        correct_pass: str = data['production_password']
        password: str | None = page.get_prod_password()
        assert password == correct_pass, (
            'Canada Post production password is not configured correctly'
        )
# FIXME: Uncomment once product attrib input is visable on page
    # def test_excluded_attrib(self,
    #                          page: ShippingMethods,
    #                          data: dict[str, Any]
    #                          ):
    #     page.navigate_tab_product_attrib()
    #     correct_exclude: list[str] = data['excluded_attributes']
    #     exclude: list[str] = page.get_excluded_attribs()
    #     assert exclude == correct_exclude, (
    #             'Excluded attributes are not configured correctly'
    #     )


class TestLetterMail:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        page: ShippingMethods
        if driver_arg:
            page = ShippingMethods(driver_arg)
        else:
            page = ShippingMethods()

        if environment == 'staging':
            page.login_staging()

        if environment == 'production':
            page.login_prod()

        if environment == 'uat':
            page.login_uat()

        return page

    @pytest.fixture(
        scope='class',
        params=glob('testcases_json/configs/shipping_methods/canada_post/letter_mail/*.json')  # noqa: E501
    )
    def data(self,
             request: FixtureRequest,
             page: ShippingMethods,
             environment: str
             ) -> dict[str, Any]:
        """ Paramitize for multiple json test cases """
        fp: str = cast(str, request.param)
        with open(fp) as file:
            data: dict[str, Any] = json.load(file)

            if environment == 'staging':
                page.navigate(cast(str, data['staging_url']))

            if environment == 'production':
                page.navigate(cast(str, data['production_url']))

            if environment == 'uat':
                page.navigate(cast(str, data['uat_url']))

            sleep(0.5)
            return data

    # ============= Tests ============= #

    def test_name(self, page: ShippingMethods, data: dict[str, Any]):
        correct_name: str = data['shipping_method_name']
        name = page.get_name()
        assert name == correct_name, (
                'The name of the shipping method is incorrect'
        )

    def test_provider(self, page: ShippingMethods, data: dict[str, Any]):
        correct_provider: str = data['provider']
        provider = page.get_shipping_provider()
        assert provider == correct_provider, (
                'The shipping provider is incorrect'
        )

    def test_routes(self, page: ShippingMethods, data: dict[str, Any]):
        correct_routes: str = data['routes']
        routes: str | None = page.get_routes()
        assert routes == correct_routes, 'The routes is incorrect'

    def test_margin_rate(self, page: ShippingMethods, data: dict[str, Any]):
        correct_rate: str = data['margin']
        rate: str | None = page.get_margin()
        assert rate == correct_rate, 'The Margin on Rate is incorrect'

    def test_add_margin(self, page: ShippingMethods, data: dict[str, Any]):
        correct_add: str = data['additional_margin']
        add: str | None = page.get_add_margin()
        assert add == correct_add, 'Additional Margin is incorrect'

    def test_product_category(self,
                              page: ShippingMethods,
                              data: dict[str, Any]
                              ):
        correct_val: str = data['product_category']
        val: str | None = page.get_product_category()
        assert val == correct_val, 'Product category is incorrect'

    def test_delivery_product(self,
                              page: ShippingMethods,
                              data: dict[str, Any]
                              ):
        correct_product: str = data['delivery_product']
        product: str | None = page.get_delivery_product()
        assert product == correct_product, (
            'Delivery Product is not configured correctly'
        )

    def test_related_company(self,
                             page: ShippingMethods,
                             data: dict[str, Any]
                             ):
        correct_state: str = data['related_company_switch']
        state: str = str(page.get_related_company())
        assert state == correct_state, 'Related to companies is not on'
        if correct_state:
            correct_list: list[str] = data['related_company_list']
            companies: list[str] = page.opt_company_names()
            assert companies == correct_list, (
                'The list of companies is not equal configured correctly'
            )

    # =============== Destination Availability=============== #
    def test_countries(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_destination()
        correct_countries: list[str] = data['country_list']
        countries: list[str] = page.get_countries()
        assert countries == correct_countries, (
                'The list of countries is not configured correctly'
        )

    def test_states(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_destination()
        correct_states: list[str] = data['state_list']
        states: list[str] = page.get_states()
        assert states == correct_states, (
                'The list of states is not configured correctly'
        )

    def test_zip_prefix(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_destination()
        correct_prefix: list[str] = data['zip_prefix_list']
        prefix: list[str] = page.get_zip_prefix()
        assert prefix == correct_prefix, (
                'The zip prefix is not configured correctly'
        )

    # ==================Extra Tab================== #
    def test_default_weight(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_extra()
        correct_default: str = data['default_weight']
        default: str | None = page.get_default_weight()
        assert default == correct_default, (
                'the default weight is not configured correctly'
        )

    def test_shipping_uom(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_extra()
        correct_uom: str = data['shipping_uom']
        uom: str | None = page.get_shipping_uom()
        assert uom == correct_uom, (
                'The shipping unit of measure is not configured correctly'
        )

    def test_packaging(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_extra()
        correct_package: str = data['packaging']
        package: str | None = page.get_packaging()
        assert package == correct_package, (
                'The packaging is not configured correctly'
        )

    def test_void_ship(self, page: ShippingMethods, data: dict[str, Any]):
        page.navigate_tab_extra()
        correct_state: str = data['void_shipment_switch']
        state: str = str(page.get_void_ship())
        assert state == correct_state, 'Void shipment is not on'

    def test_service_type(self, page: ShippingMethods, data: dict[str, Any]):
        correct_service: str = data['service_type']
        service: str | None = page.get_service_type()
        assert service == correct_service, (
                'Service type was not configured correctly'
        )
    # ==================Product Attrib Tab================== #
    def test_excluded_attrib(self,
                             page: ShippingMethods,
                             data: dict[str, Any]
                             ):
        page.navigate_tab_product_attrib()
        correct_exclude: list[str] = data['excluded_attributes']
        exclude: list[str] = page.get_excluded_attribs()
        assert exclude == correct_exclude, (
                'Excluded attributes are not configured correctly'
        )
