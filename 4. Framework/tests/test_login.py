from pages.login_page import LoginPage


def test_login_url(driver):
    driver.get(LoginPage.URL)
    assert driver.current_url == LoginPage.URL


def test_login_title(driver):
    driver.get(LoginPage.URL)
    assert driver.title == "MantisBT"


def test_successful_login(mantis_site):
    mantis_site.login("admin", "admin20")
    assert mantis_site.main_page.get_user_name() == "admin"