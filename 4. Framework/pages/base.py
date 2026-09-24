from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:
    RECENT_ISSUE_LINK = (By.CSS_SELECTOR, "div.nav-recent a")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def find_element(self, locator: tuple[str, str]):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    def find_all_elements(self, locator: tuple[str, str]):
        return self.wait.until(expected_conditions.presence_of_all_elements_located(locator))

    def get_last_issue_id(self) -> str:
        return self.find_element(self.RECENT_ISSUE_LINK).text