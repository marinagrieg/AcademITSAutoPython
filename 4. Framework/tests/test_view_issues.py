def test_issues_count(mantis_site):
    mantis_site.login("admin", "admin20")
    mantis_site.main_page.open_view_issues_page()

    assert mantis_site.view_issues_page.count_issues() == 50