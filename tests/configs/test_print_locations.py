
import json
from glob import glob
from time import sleep
from typing import Any, cast

import pytest
from pages.configs.print_locations import PrintLocations
from pytest import FixtureRequest


class TestPrintingLocations:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest) -> PrintLocations:
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        page: PrintLocations

        if driver_arg:
            page = PrintLocations(driver_arg)
        else:
            page = PrintLocations()

        if environment == 'staging':
            page.login_staging()

        if environment == 'production':
            page.login_prod()

        if environment == 'uat':
            page.login_uat()

        return page

    @pytest.fixture(
        scope='class',
        params=glob('testcases_json/configs/print_locations/*.json')
    )
    def data(self,
             request: FixtureRequest,
             page: PrintLocations,
             environment: str
             ) -> dict[str, Any]:
        """Paramitize for multiple json test cases"""
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

    def test_location_struct(self, page: PrintLocations, data: dict[str, Any]):
        correct_val: list[list[str]] = data['location_struct']
        val: list[list[str]] = page.get_locations()
        assert val == correct_val, 'One or more print locations are incorrect'
