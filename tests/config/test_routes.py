import json
from glob import glob
from time import sleep

import pytest
from pages.routes import Routes
from pytest import FixtureRequest


class TestArtworkManifestSettings:
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
        return page

    @pytest.fixture(
        scope='class',
        params=glob('testcases_json/routes/*.json')
    )
    def data(self, request: FixtureRequest, page: Routes, environment: str):
        """Paramitize for multiple json test cases"""
        with open(request.param, 'r') as file:
            data = json.load(file)
            if environment == 'staging':
                page.navigate(data['staging_url'])

            if environment == 'production':
                page.navigate(data['production_url'])

            sleep(0.5)
            return data
# ========== tests ========== #
