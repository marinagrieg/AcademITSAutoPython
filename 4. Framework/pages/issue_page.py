from selenium.webdriver.common.by import By

from pages.base import BasePage


class IssuePage(BasePage):
    ISSUE_ID = (By.CSS_SELECTOR, "td.bug-id")
    CATEGORY = (By.CSS_SELECTOR, "td.bug-category")
    SUMMARY = (By.CSS_SELECTOR, "td.bug-summary")
    DESCRIPTION = (By.CSS_SELECTOR, "td.bug-description")
    DELETE_BUTTON = (By.CSS_SELECTOR, "input[value='Delete']")
    CONFIRM_DELETE_BUTTON = (By.CSS_SELECTOR, "input[value='Delete Issues']")

    def get_issue_id(self) -> str:
        return self.find_element(self.ISSUE_ID).text

    def get_category(self) -> str:
        return self.find_element(self.CATEGORY).text

    def get_summary(self) -> str:
        return self.find_element(self.SUMMARY).text

    def get_description(self) -> str:
        return self.find_element(self.DESCRIPTION).text

    def delete(self) -> None:
        self.find_element(self.DELETE_BUTTON).click()
        self.find_element(self.CONFIRM_DELETE_BUTTON).click()