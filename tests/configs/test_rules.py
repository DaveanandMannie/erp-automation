import json
from glob import glob
from time import sleep
from typing import Any, cast

import pytest
from pages.configs.rules import Rules
from pytest import FixtureRequest


class TestRules:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        page: Rules

        if driver_arg:
            page = Rules(driver_arg)
        else:
            page = Rules()

        if environment == 'staging':
            page.login_staging()

        if environment == 'production':
            page.login_prod()

        if environment == 'uat':
            page.login_uat()

        return page

    @pytest.fixture(
        scope='class',
        params=glob('testcases_json/configs/rules/*.json')
    )
    def data(self,
             request: FixtureRequest,
             page: Rules,
             environment: str) -> dict[str, Any]:
        """Paramitize for multiple json test cases"""
        fp: str = cast(str, request.param)
        with open(fp, encoding='utf-8') as file:
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

    def test_name(self, page: Rules, data: dict[str, Any]):
        correct_val: str = data['name']
        val: str | None = page.get_name()
        assert val == correct_val, 'Name is not configured correctly'

    def test_action(self, page: Rules, data: dict[str, Any]):
        correct_val: str = data['action']
        val: str = page.get_action()
        assert val == correct_val, (
            f'Action is not configured correctly for rule: {data['name']}'
            )

    def test_opt_type(self, page: Rules, data: dict[str, Any]):
        correct_val: str = data['operation_type']
        val: str | None = page.get_opt_type()
        assert val == correct_val, (
            f'Operation type is not configured correctly for rule: {data['name']}'  # noqa: E501
        )

    def test_src(self, page: Rules, data: dict[str, Any]):
        if data['action'] not in ['Pull From', 'Manufacture']:
            pytest.skip(f'Skipping source test in {data['name']}')

        correct_val: str = data['source']
        val: str | None = page.get_src_location()
        assert val == correct_val, (
            f'Source location is not configured correctly for rule: {data['name']}'  # noqa:E501
        )

    def test_destination(self, page: Rules, data: dict[str, Any]):
        correct_val: str = data['destination']
        val: str | None = page.get_dest_location()
        assert val == correct_val, (
            f'Destination location is not configured correctly for rule: {data['name']}'  # noqa: E501
        )

    def test_supply_method(self, page: Rules, data: dict[str, Any]):
        if data['action'] != 'Pull From':
            pytest.skip(f'Skipping supply method test in {data['name']}')

        correct_val: str = data['supply_method']
        val: str = page.get_supply_method()
        assert val == correct_val, (
            f'Supply method is not configured correctly for rule: {data['name']}'  # noqa: E501
        )

    def test_route(self, page: Rules, data: dict[str, Any]):
        correct_val: str = data['route']
        val: str | None = page.get_route()
        assert val == correct_val, (
            f'Routes is not configured correctly for rule: {data['name']}'
        )

    def test_partner_addy(self, page: Rules, data: dict[str, Any]):
        if data['action'] != 'Pull From':
            pytest.skip(f'Skipping Pull From specfic test in {data['name']}')

        correct_val: str = data['partner_address']
        val: str | None = page.get_partner_address()
        assert val == correct_val, (
            f'Partner address is not configured correctly for rule: {data['name']}'  # noqa: E501
        )

    def test_lead_time(self, page: Rules, data: dict[str, Any]):
        if data['action'] != 'Pull From':
            pytest.skip(f'Skipping Pull From specfic test in {data['name']}')

        correct_val: str = data['lead_time']
        val: str | None = page.get_lead_time()
        assert val == correct_val, (
            f'Lead time is not configured correctly for rule: {data['name']}'
        )
