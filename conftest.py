import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Unknown browser: {browser}")

    driver.maximize_window()

    yield driver

    driver.quit()