import json
from glob import glob
from time import sleep

import pytest
from pages.product_categories import ProductCategory
from pytest import FixtureRequest


# TODO: wait untill Daniel and Rabie finsish with the GL Mapping
# TODO: decide to decode json
class TestFinishedProductCategories:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        if driver_arg:
            page: ProductCategory = ProductCategory(driver_arg)
        else:
            page: ProductCategory = ProductCategory()

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
            'testcases_json/configs/product_categories/finished/*.json'
        )
    )
    def data(self, request: FixtureRequest, page: ProductCategory, environment: str):  # noqa: E501
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

    def test_name(self, page: ProductCategory, data: dict):
        correct_val: str = data['name']
        name: str | None = page.get_name()
        assert name == correct_val, f'Incorrect Category name: {data['name']}'

    def test_parent_category(self, page: ProductCategory, data: dict):
        correct_cat: str = data['parent_category']
        cat: str | None = page.get_parent_category()
        assert cat == correct_cat, f'Incorrect Parent category: {data['name']}'

    def test_general_categoroy(self, page: ProductCategory, data: dict):
        cor_val: str = data['is_general_category']
        val: str = str(page.get_general_category())
        assert val == cor_val, f'Incorrect General category: {data['name']}'

    def test_require_pallet(self, page: ProductCategory, data: dict):
        correct_val: str = data['required_pallet']
        val: str = str(page.get_require_pallet())
        assert val == correct_val, f'Incorrect Require pallet: {data['name']}'

    def test_require_profile(self, page: ProductCategory, data: dict):
        cor_val: str = data['required_profile']
        val: str = str(page.get_require_profile())
        assert val == cor_val, f'Incorrect Require profile: {data['name']}'

    def test_require_batching(self, page: ProductCategory, data: dict):
        cor_val: str = data['required_batching']
        val: str = str(page.get_require_batching())
        assert val == cor_val, f'Incorrect Require batching: {data['name']}'

    def test_require_binning(self, page: ProductCategory, data: dict):
        correct_val: str = data['required_binning']
        val: str = str(page.get_require_binning())
        assert val == correct_val, f'Incorrect Require binning:{data['name']}'

    def test_bin_by(self, page: ProductCategory, data: dict):
        correct_val: str = data['product_bin_by']
        val: str = page.get_bin_by()
        assert val == correct_val, f'Incorrect Product bin by:{data['name']}'

    def test_routes(self, page: ProductCategory, data: dict):
        correct_list: list = data['routes']
        route_list: list = page.get_routes()
        assert route_list == correct_list, f'Inccorect Routes:{data['name']}'

    def test_total_routes(self, page: ProductCategory, data: dict):
        cor_val: list = data['total_routes']
        route_list: list = page.get_total_routes()
        assert route_list == cor_val, f'Incorrect Total routes: {data['name']}'

    def test_removal_strat(self, page: ProductCategory, data: dict):
        cor_val: str = data['removal_strategy']
        val: str | None = page.get_removal_strategy()
        assert val == cor_val, f'Incorrect Removal strategy: {data['name']}'

    def test_cost_method(self, page: ProductCategory, data: dict):
        correct_val: str = data['costing_method']
        val: str = page.get_costing_methods()
        assert val == correct_val, f'Incorrect Costing method: {data['name']}'

    def test_inventory_valuation(self, page: ProductCategory, data: dict):
        cor_val: str = data['inventory_valuation']
        val: str = page.get_valuation()
        assert val == cor_val, f'Incorrect Inventory valuation: {data['name']}'

    def test_print_profile(self, page: ProductCategory, data: dict):
        correct_val: str = data['print_profile']
        val: str | None = page.get_print_profile()
        assert val == correct_val, f'Incorrect Print profile: {data['name']}'

    def test_pallet_type(self, page: ProductCategory, data: dict):
        correct_val: str = data['pallet_type']
        val: str | None = page.get_pallet_type()
        assert val == correct_val, f'Incorrect Pallet type: {data['name']}'

    def test_file_format(self, page: ProductCategory, data: dict):
        cor_val: str = data['filename_format']
        val: str | None = page.get_file_name()
        assert val == cor_val, f'Incorrect File name format: {data['name']}'


class TestRawProductCategories:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest):
        """ Selenium driver with scraper """
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        if driver_arg:
            page: ProductCategory = ProductCategory(driver_arg)
        else:
            page: ProductCategory = ProductCategory()

        if environment == 'staging':
            page.login_staging()

        if environment == 'production':
            page.login_prod()

        if environment == 'uat':
            page.login_uat()

        return page

    @pytest.fixture(
        scope='class',
        params=glob('testcases_json/configs/product_categories/raw/*.json')
    )
    def data(self, request: FixtureRequest, page: ProductCategory, environment: str):  # noqa: E501
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

    # ============ Tests ============ #

    def test_name(self, page: ProductCategory, data: dict):
        correct_name: str = data['name']
        name: str | None = page.get_name()
        assert name == correct_name, f'Incorrect Category name: {data['name']}'

    def test_parent_category(self, page: ProductCategory, data: dict):
        correct_cat: str = data['parent_category']
        cat: str | None = page.get_parent_category()
        assert cat == correct_cat, f'Incorrect Parent category: {data['name']}'

    def test_general_categoroy(self, page: ProductCategory, data: dict):
        cor_val: str = data['is_general_category']
        val: str = str(page.get_general_category())
        assert val == cor_val, f'Incorrect General category: {data['name']}'

    def test_routes(self, page: ProductCategory, data: dict):
        correct_list: list = data['routes']
        route_list: list = page.get_routes()
        assert route_list == correct_list, f'Incorrect Routes: {data['name']}'

    def test_total_routes(self, page: ProductCategory, data: dict):
        if data['name'] == 'Shipping':
            pytest.skip('Skipping total routes test on "Shipping"')
        if data['name'] == 'Consumable':
            pytest.skip('Skipping total routes test on "Consumable"')
        if data['name'] == 'All':
            pytest.skip('Skipping total routes test on "All"')
        if data['name'] == 'Raw':
            pytest.skip('Skipping total routes test on "raw"')
        if data['name'] == 'Finished':
            pytest.skip('Skipping total routes test on "Finished"')

        cor_list: list = data['total_routes']
        route_val: list = page.get_total_routes()
        assert route_val == cor_list, f'Incorrect Total routes: {data['name']}'

    def test_removal_strat(self, page: ProductCategory, data: dict):
        cor_val: str = data['removal_strategy']
        val: str | None = page.get_removal_strategy()
        assert val == cor_val, f'Incorrect Removal strategy: {data['name']}'

    def test_cost_method(self, page: ProductCategory, data: dict):
        correct_val: str = data['costing_method']
        val: str = page.get_costing_methods()
        assert val == correct_val, f'Incorrect Costing method: {data['name']}'

    def test_inventory_valuation(self, page: ProductCategory, data: dict):
        cor_val: str = data['inventory_valuation']
        val: str = page.get_valuation()
        assert val == cor_val, f'Incorrect Inventory valuation: {data['name']}'

    def test_print_profile(self, page: ProductCategory, data: dict):
        correct_val: str = data['print_profile']
        val: str | None = page.get_print_profile()
        assert val == correct_val, f'Incorrect Print profile: {data['name']}'

    def test_pallet_type(self, page: ProductCategory, data: dict):
        correct_val: str = data['pallet_type']
        val: str | None = page.get_pallet_type()
        assert val == correct_val, f'Incorrect Pallet type: {data['name']}'
