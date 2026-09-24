from datetime import datetime

import pytest_check as check


def test_create_and_delete_issue(mantis_site):
    timestamp = f"{datetime.now():%d-%m-%Y %H:%M:%S}"

    category = "[All Projects] General"
    summary = f"Summary {timestamp}"
    description = f"Description {timestamp}"

    mantis_site.login("admin", "admin20")
    mantis_site.main_page.go_to_report_issues_page()

    mantis_site.report_issue_page.create_issue(category, summary, description)

    mantis_site.report_issue_page.wait_for_redirect()
    issue_id = mantis_site.report_issue_page.get_last_issue_id()

    mantis_site.view_issues_page.open_view_issues_page()
    mantis_site.view_issues_page.open_issue(issue_id)

    check.equal(mantis_site.issue_page.get_issue_id(), issue_id)
    check.is_in(summary, mantis_site.issue_page.get_summary())
    check.equal(mantis_site.issue_page.get_description(), description)
    check.equal(mantis_site.issue_page.get_category(), category)

    mantis_site.issue_page.delete()

    assert not mantis_site.view_issues_page.has_issue(issue_id)