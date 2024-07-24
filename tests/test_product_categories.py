import json
from glob import glob
from time import sleep

import pytest
from pages.product_category import ProductCategory


class TestProductCategories:
    @pytest.fixture(scope='class')
    def page(self, request):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')
        page: ProductCategory = ProductCategory('--headless')

        if environment == 'staging':
            page.login_staging()
        if environment == 'production':
            page.login_prod()
        return page

    @pytest.fixture(
        scope='class',
        params=glob('testcases_json/product_categories/finished/*.json')
    )
    def data(self, request, page: ProductCategory, environment: str):
        """Paramitize for multiple json test cases"""
        with open(request.param, 'r') as file:
            data = json.load(file)
            if environment == 'staging':
                page.navigate(data['staging_url'])

            if environment == 'production':
                page.navigate(data['production_url'])

            sleep(0.5)
            return data

    # ============= Tests ============= #

    def test_name(self, page: ProductCategory, data: dict):
        correct_name: str = data['name']
        name: str = page.get_name()
        assert name == correct_name, (
            f'Category name is not configured correctly: {data['name']}'
        )

    def test_parent_category(self, page: ProductCategory, data: dict):
        correct_cat: str = data['parent_category']
        cat: str = page.get_parent_category()
        assert cat == correct_cat, (
            f'Parent category is not configured correct: {data['name']}'
        )

    def test_general_categoroy(self, page: ProductCategory, data: dict):
        correct_val: bool = bool(data['is_general_category'])
        val: bool = page.get_general_category()
        assert val == correct_val, (
            f'General category is not configured correctly: {data['name']}'
        )

    def test_require_pallet(self, page: ProductCategory, data: dict):
        correct_val: bool = bool(data['required_pallet'])
        val: bool = page.get_require_pallet()
        assert val == correct_val, (
            f'require pallet is not configured correctly: {data['name']}'
        )
