import pytest

from pages.mantis_site import MantisSite


@pytest.fixture
def mantis_site(driver):
    return MantisSite(driver)