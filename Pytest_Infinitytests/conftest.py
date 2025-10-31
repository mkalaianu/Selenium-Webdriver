import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome", help="browser selection"
    )
@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "Chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
    elif browser_name == "Edge":
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.implicitly_wait(5)
    yield driver
    driver.close

