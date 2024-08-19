import json
from glob import glob
from time import sleep

import pytest
from pages.configs.routes import Routes
from pytest import FixtureRequest


class TestProductCategories:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        if driver_arg:
            page: Routes = Routes(driver_arg)
        else:
            page: Routes = Routes()

        if environment == 'staging':
            page.login_staging()

        if environment == 'production':
            page.login_prod()

        if environment == 'uat':
            page.login_uat()
        return page

    @pytest.fixture(
        scope='class',
        params=glob('testcases_json/configs/routes/*.json')
    )
    def data(self, request: FixtureRequest, page: Routes, environment: str):
        """Paramitize for multiple json test cases"""
        with open(request.param, 'r') as file:
            data = json.load(file)
            if environment == 'staging':
                page.navigate(data['staging_url'])

            if environment == 'production':
                page.navigate(data['production_url'])

            if environment == 'uat':
                page.navigate(data['uat_url'])

            sleep(0.9)
            return data
# ========== tests ========== #

    def test_name(self, page: Routes, data: dict):
        correct_val: str = data['name']
        val: str = page.get_name()
        assert val == correct_val, (
            f'Name is not configured correctly for route: {correct_val}'
        )

    def test_product_categories(self, page: Routes, data: dict):
        correct_val: str = data['product_categories']
        val: str = str(page.get_product_category_bool())
        assert val == correct_val, (
            f'Applied on product categories is not correct for route: {correct_val}'  # noqa: E501
        )

    def test_products(self, page: Routes, data: dict):
        correct_val: str = data['products']
        val: str = str(page.get_products_bool())
        assert val == correct_val, (
            f'Applied on products is not correct for route: {correct_val}'
        )

    def test_warehouses(self, page: Routes, data: dict):
        correct_val: str = data['warehouses']

        if correct_val == 'True':
            opt: list = page.opt_get_warehouse_ids()
            correct_opt: list = data['warehouse_ids']
            assert opt == correct_opt, (
                f'List of warehouses not configured correctly for route: {data['name']}'  # noqa: E501
            )

        val: str = str(page.get_warehouses_bool())
        assert val == correct_val, (
            f'Applied on warehouses is not correct for route: {correct_val}'
        )

    def test_sales_lines(self, page: Routes, data: dict):
        correct_val: str = data['sales_lines']
        val: str = str(page.get_sales_lines_bool())
        assert val == correct_val, (
            f'Applied on sales lines is not correct for route: {correct_val}'
        )

    def test_rules(self,  page: Routes, data: dict):
        correct_val: list = data['rules']
        val: list = page.get_rules()
        assert val == correct_val, (
            f'One or more rules is not configured correctly for route {correct_val}'  # noqa: E501
        )
