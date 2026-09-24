from selenium.webdriver.remote.webdriver import WebDriver

from pages.issue_page import IssuePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.password_page import PasswordPage
from pages.report_issue_page import ReportIssuePage
from pages.view_issues_page import ViewIssuesPage


class MantisSite:
    def __init__(self, driver: WebDriver):
        self.login_page = LoginPage(driver)
        self.password_page = PasswordPage(driver)
        self.main_page = MainPage(driver)
        self.view_issues_page = ViewIssuesPage(driver)
        self.issue_page = IssuePage(driver)
        self.report_issue_page = ReportIssuePage(driver)

    def login(self, login: str, password: str) -> None:
        self.login_page.login(login)
        self.password_page.login(password)