import pytest
from pytest import Parser, FixtureRequest


def pytest_addoption(parser: Parser):
    parser.addoption(
        '--environment',
        action='store',
        default='staging',
        help='Choose a enviroenmet'
    )


@pytest.fixture(scope='session')
def environment(request: FixtureRequest):
    """Fixture to get the environment argument."""
    return request.config.getoption('--environment')
