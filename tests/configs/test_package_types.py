import json
from glob import glob
from time import sleep

import pytest
from pages.package_types import PackageTypes
from pytest import FixtureRequest


# TODO: Port to Odoo 17
class TestArtworkManifestSettings:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        if driver_arg:
            page: PackageTypes = PackageTypes(driver_arg)
        else:
            page: PackageTypes = PackageTypes()

        if environment == 'staging':
            page.login_staging()

        if environment == 'production':
            page.login_prod()

        if environment == 'uat':
            page.login_uat()
        return page

    @pytest.fixture(
        scope='class',
        params=glob('testcases_json/configs/package_types/*.json')
    )
    def data(self, request: FixtureRequest, page: PackageTypes, environment: str):  # noqa: E501
        """Paramitize for multiple json test cases"""
        with open(request.param, 'r') as file:
            data = json.load(file)
            if environment == 'staging':
                page.navigate(data['staging_url'])

            if environment == 'production':
                page.navigate(data['production_url'])

            if environment == 'uat':
                page.navigate(data['uat_url'])
            sleep(0.5)
            return data
    # ============= Tests ============= #

    def test_name(self, page: PackageTypes, data: dict):
        correct_val: str = data['name']
        val: str = page.get_name()
        assert val == correct_val, 'Name is not configured correclty'

    def test_dimensions(self, page: PackageTypes, data: dict):
        correct_val: list = data['dimensions']
        val: list = page.get_dimensions()
        assert val == correct_val, (
            f'Dimensions is not configured correctly for :{data['name']}'
        )

    def test_weight(self, page: PackageTypes, data: dict):
        correct_val: str = data['weight']
        val: str = page.get_weight()
        assert val == correct_val, (
            f'Weight is not configured correctly for: {data['name']}'
        )

    def test_max_weight(self, page: PackageTypes, data: dict):
        correct_val: str = data['max_weight']
        val: str = page.get_max_weight()
        assert val == correct_val, (
            f'Max weight is not configured correctly for: {data['name']}'
        )

    def test_barcode(self, page: PackageTypes, data: dict):
        correct_val: str = data['barcode']
        val: str = page.get_barcode()
        assert val == correct_val, (
            f'Barcode is not configured correctly for: {data['name']}'
        )

    def test_price(self, page: PackageTypes, data: dict):
        correct_val: str = data['price']
        val: str = page.get_price()
        assert val == correct_val, (
            f'Price is not configured correctly for: {data['name']}'
        )

    def test_clients(self, page: PackageTypes, data: dict):
        correct_val: str = data['related_to_client']
        val: str = str(page.get_related_to_client())
        assert val == correct_val, (
            f'Related to client is not toggled correctly for: {data['name']}'
        )
        if val == 'True':
            correct_vals: list = data['companies']
            vals: list = page.opt_get_companies()
            assert vals == correct_vals, f'List of companies is not configured correctly for: {data['name']}'  # noqa: E501

    def test_product(self, page: PackageTypes, data: dict):
        correct_val: str = data['product']
        val: str = page.get_product()
        assert val == correct_val, (
            f'Product is not configured correctly for: {data['name']}'
        )

    def test_package_rules(self, page: PackageTypes, data: dict):
        correct_val: list = data['package_rules']
        val: list = page.get_package_rules()
        assert val == correct_val, (
            f'Package rules is not configured correctly for: {data['name']}'
        )
