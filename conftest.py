import pytest
from driver_maker import DriverMaker


@pytest.fixture()
def setUp():
    print("Initiating the setUp method, stay tuned...")
    yield
    print("Initiating the tearDown method...")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    """
    Takes in browser parameter passed from the command line and calls DriverMaker class to create the new driver.
    """
    print("Starting one time setUp method")
    dm = DriverMaker(browser)
    driver = dm.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Starting one time tearDown")


def pytest_addoption(parser):
    """
    Creates options to enter browser ans OS versions via command line to parser.
    """
    parser.addoption("--browser")
    parser.addoption("--osType")


@pytest.fixture(scope="session")
def browser(request):
    """
    Returns browser option entered from command line
    """
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    """
    Returns browser option entered from command line
    """
    return request.config.getoption("--osType")
