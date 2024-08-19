import json
from glob import glob
from time import sleep

import pytest
from pages.configs.service_types import ServiceType
from pytest import FixtureRequest


# TODO: decide to decode json
class TestServicetypes:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        if driver_arg:
            page: ServiceType = ServiceType(driver_arg)
        else:
            page: ServiceType = ServiceType()

        if environment == 'staging':
            page.login_staging()

        if environment == 'production':
            page.login_prod()

        if environment == 'uat':
            page.login_uat()
        return page

    @pytest.fixture(
        scope='class',
        params=glob('testcases_json/configs/service_types/odoo_17/*.json')
    )
    def data(self, request: FixtureRequest, page: ServiceType, environment: str):  # noqa: E501
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

    def test_entire_page(self, page: ServiceType, data: dict):
        correct_val: list[list[str]] = data['struct']
        val: list[list[str]] = page.get_service_struct()
        assert val == correct_val, '1 or more service types are incorrect'
