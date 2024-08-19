import json
from glob import glob
from time import sleep

import pytest
from pages.configs.artworkmanifest import ManifestSettings
from pytest import FixtureRequest


class TestArtworkManifestSettings:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        if driver_arg:
            page: ManifestSettings = ManifestSettings(driver_arg)
        else:
            page: ManifestSettings = ManifestSettings()

        if environment == 'staging':
            page.login_staging()

        if environment == 'production':
            page.login_prod()

        if environment == 'uat':
            page.login_uat()
        return page

    @pytest.fixture(
        scope='class',
        params=glob('testcases_json/configs/artworkmanifest_settings/*.json')
    )
    def data(self, request: FixtureRequest, page: ManifestSettings, environment: str):  # noqa: E501
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

    def test_manifest_settings(self, page: ManifestSettings, data: dict):
        correct_settings: list = data['settings']
        settings: list = page.get_manifest_fields()
        assert settings == correct_settings, (
            'Artwork Manifest Settings not configured correctly'
        )
