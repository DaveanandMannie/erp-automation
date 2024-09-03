import json
from glob import glob
from time import sleep
from typing import Any, cast

import pytest
from pages.configs.routes import Routes
from pytest import FixtureRequest


class TestProductCategories:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        page: Routes
        if driver_arg:
            page = Routes(driver_arg)
        else:
            page = Routes()

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
    def data(self,
             request: FixtureRequest,
             page: Routes,
             environment: str
             ) -> dict[str, Any]:
        """Paramitize for multiple json test cases"""
        fp: str = cast(str, request.param)
        with open(fp, 'r') as file:
            data: dict[str, Any] = json.load(file)
            if environment == 'staging':
                page.navigate(cast(str, data['staging_url']))

            if environment == 'production':
                page.navigate(cast(str, data['production_url']))

            if environment == 'uat':
                page.navigate(cast(str, data['uat_url']))

            sleep(0.9)
            return data
# ========== tests ========== #

    def test_name(self, page: Routes, data: dict[str, Any]):
        sleep(0.2)
        correct_val: str = data['name']
        val: str | None = page.get_name()
        assert val == correct_val, (
            f'Name is not configured correctly for route: {correct_val}'
        )

    def test_product_categories(self, page: Routes, data: dict[str, Any]):
        correct_val: str = data['product_categories']
        val: str = str(page.get_product_category_bool())
        assert val == correct_val, (
            f'Applied on product categories is not correct for route: {correct_val}'  # noqa: E501
        )

    def test_products(self, page: Routes, data: dict[str, Any]):
        correct_val: str = data['products']
        val: str = str(page.get_products_bool())
        assert val == correct_val, (
            f'Applied on products is not correct for route: {correct_val}'
        )

    def test_warehouses(self, page: Routes, data: dict[str, Any]):
        correct_val: str = data['warehouses']

        if correct_val == 'True':
            opt: list[str] = page.opt_get_warehouse_ids()
            correct_opt: list[str] = data['warehouse_ids']
            assert opt == correct_opt, (
                f'List of warehouses not configured correctly for route: {data['name']}'  # noqa: E501
            )

        val: str = str(page.get_warehouses_bool())
        assert val == correct_val, (
            f'Applied on warehouses is not correct for route: {correct_val}'
        )

    def test_sales_lines(self, page: Routes, data: dict[str, Any]):
        correct_val: str = data['sales_lines']
        val: str = str(page.get_sales_lines_bool())
        assert val == correct_val, (
            f'Applied on sales lines is not correct for route: {correct_val}'
        )

    def test_rules(self,  page: Routes, data: dict[str, Any]):
        correct_val: list[list[str]] = data['rules']
        val: list[list[str]] = page.get_rules()
        assert val == correct_val, (
            f'One or more rules is not configured correctly for route {correct_val}'  # noqa: E501
        )
