import json
from glob import glob
from time import sleep
from typing import Any, cast

import pytest
from pytest import FixtureRequest

from pages.configs.artworkmanifest import ManifestSettings


class TestArtworkManifestSettings:
    @pytest.fixture(scope='class')
    def page(self, request: FixtureRequest):
        """ Selenium driver with scraper """
        environment: str = request.config.getoption('--environment')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        driver_arg: str = request.config.getoption('--window')  # pyright: ignore[reportAssignmentType]  # noqa: E501
        page: ManifestSettings
        if driver_arg:
            page = ManifestSettings(driver_arg)
        else:
            page = ManifestSettings()

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
    def data(self,
             request: FixtureRequest,
             page: ManifestSettings,
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

    def test_manifest_settings(self,
                               page: ManifestSettings,
                               data: dict[str, Any],
                               environment: str,
                               ):
# FIXME: remove once my privilages are updated
        if environment != 'production':
            pytest.skip('waiting on prod refresh')
        correct_settings: list[str] = data['settings']
        settings: list[str] = page.get_manifest_fields()
        assert settings == correct_settings, (
            'Artwork Manifest Settings not configured correctly'
        )
