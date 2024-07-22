import pytest
import logging


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


# TODO: do I want to supress this ?
def pytest_configure(config):
    logging.getLogger('selenium').setLevel(logging.ERROR)
