from selenium.webdriver.common.by import By

from pages.base import BasePage


class ViewIssuesPage(BasePage):
    ISSUE_ID_CELLS = (By.CSS_SELECTOR, "td.column-id")
    ISSUE_LINK_TEMPLATE = "//td[@class='column-id']/a[text()='{}']"
    URL = "https://academ-it.ru/mantisbt/view_all_bug_page.php"

    def count_issues(self) -> int:
        return len(self.find_all_elements(self.ISSUE_ID_CELLS))

    def open_issue(self, issue_id: str) -> None:
        locator = (By.XPATH, self.ISSUE_LINK_TEMPLATE.format(issue_id))
        self.find_element(locator).click()

    def has_issue(self, issue_id: str) -> bool:
        locator = (By.XPATH, self.ISSUE_LINK_TEMPLATE.format(issue_id))
        return len(self.driver.find_elements(*locator)) > 0

    def open_view_issues_page(self) -> None:
        self.driver.get(self.URL)