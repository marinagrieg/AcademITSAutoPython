from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base import BasePage


class PasswordPage(BasePage):
    PASSWORD_FIELD = (By.ID, "password")

    def login(self, password: str) -> None:
        self.find_element(self.PASSWORD_FIELD).send_keys(password, Keys.ENTER)