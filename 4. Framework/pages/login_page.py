from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base import BasePage


class LoginPage(BasePage):
    URL: str = "https://academ-it.ru/mantisbt/login_page.php"
    LOGIN_FIELD = (By.CSS_SELECTOR, "#username")

    def login(self, login: str) -> None:
        self.driver.get(self.URL)
        self.find_element(self.LOGIN_FIELD).send_keys(login, Keys.ENTER)