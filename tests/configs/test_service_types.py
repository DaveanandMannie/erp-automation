import json
from glob import glob
from time import sleep

import pytest
from pages.service_types import ServiceType
from pytest import FixtureRequest


# TODO: decide to decode json
class TestFinishedProductCategories:
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
        return page

    @pytest.fixture(
        scope='class',
        params=glob('testcases_json/configs/service_types/*.json')
    )
    def data(self, request: FixtureRequest, page: ServiceType, environment: str):  # noqa: E501
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

    def test_name(self, page: ServiceType, data: dict):
        correct_name: str = data['name']
        name: str = page.get_name()
        assert name == correct_name, f'Name not configured correctly:{data['name']}'  # noqa: E501

    def test_code(self, page: ServiceType, data: dict):
        correct_code: str = data['code']
        code: str = page.get_code()
        assert code == correct_code, f'Code not configured correctly:{data['name']}'  # noqa: E501

    def test_look_up(self, page: ServiceType, data: dict):
        correct_look_up: str = data['look_up']
        look_up: str = page.get_look_up()
        assert look_up == correct_look_up, f'Look Up not configured correctly:{data['name']}'  # noqa: E501

    def test_provider(self, page: ServiceType, data: dict):
        correct_provider: str = data['provider']
        provider: str = page.get_provider()
        assert provider == correct_provider, f'Provider not configured correctly:{data['name']}'  # noqa: E501
