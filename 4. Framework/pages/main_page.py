from selenium.webdriver.common.by import By

from pages.base import BasePage


class MainPage(BasePage):
    USER_NAME = (By.CSS_SELECTOR, "span.user-info")
    VIEW_ISSUES_BUTTON = (By.CSS_SELECTOR, "a[href='/mantisbt/view_all_bug_page.php']")
    REPORT_ISSUE_BUTTON = (By.CSS_SELECTOR, "a[href='/mantisbt/bug_report_page.php']")

    def get_user_name(self) -> str:
        return self.find_element(self.USER_NAME).text

    def go_to_view_issues_page(self) -> None:
        self.find_element(self.VIEW_ISSUES_BUTTON).click()

    def go_to_report_issues_page(self) -> None:
        self.find_element(self.REPORT_ISSUE_BUTTON).click()