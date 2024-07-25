import pytest
from pytest import FixtureRequest, Parser


def pytest_addoption(parser: Parser):
    parser.addoption(
        '--environment',
        action='store',
        default='staging',
        help='Choose a enviroenmet'
    )

    parser. addoption(
        '--window',
        action='store',
        default='headless',
        help='Choose to show the driver manipulation'

    )


@pytest.fixture(scope='session')
def environment(request: FixtureRequest):
    """Fixture to get the environment argument."""
    return request.config.getoption('--environment')


@pytest.fixture(scope='session')
def window(request: FixtureRequest):
    """Fixture to get the environment argument."""
    if not request.config.getoption('--window'):
        return None
    return request.config.getoption('--window')
