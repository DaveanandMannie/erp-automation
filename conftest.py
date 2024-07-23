import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--environment',
        action='store',
        default='staging',
        help='Choose a enviroenmet'
    )


@pytest.fixture(scope='session')
def environment(request):
    """Fixture to get the environment argument."""
    return request.config.getoption('--environment')
