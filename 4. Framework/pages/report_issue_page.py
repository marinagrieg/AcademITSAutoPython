from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions

from pages.base import BasePage


class ReportIssuePage(BasePage):
    CATEGORY = (By.ID, "category_id")
    SUMMARY = (By.ID, "summary")
    DESCRIPTION = (By.ID, "description")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[type=submit]")

    def create_issue(self, category: str, summary: str, description: str) -> None:
        category_select = Select(self.find_element(self.CATEGORY))
        category_select.select_by_visible_text(category)

        self.find_element(self.SUMMARY).send_keys(summary)
        self.find_element(self.DESCRIPTION).send_keys(description)
        self.find_element(self.SUBMIT_BUTTON).click()

    def wait_for_redirect(self) -> None:
        self.wait.until(expected_conditions.url_contains("view_all_bug_page"))