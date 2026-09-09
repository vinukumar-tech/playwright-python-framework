import pytest
import pytest_html
from playwright.sync_api import sync_playwright


# ============================================================
# PLAYWRIGHT PAGE FIXTURE
# ============================================================

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        page.set_default_timeout(30000)
        page.set_default_navigation_timeout(60000)

        yield page

        browser.close()


# ============================================================
# PYTEST HTML REPORT
# ============================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    # --------------------------------------------------------
    # CREATE EXTRAS
    # --------------------------------------------------------

    extras = getattr(report, "extras", [])

    # --------------------------------------------------------
    # REQUEST ID
    # --------------------------------------------------------

    if hasattr(item, "request_id"):
        extras.append(pytest_html.extras.text(f"Request ID: {item.request_id}", name="Request ID"))

    # --------------------------------------------------------
    # REQUEST STATUS
    # --------------------------------------------------------

    if hasattr(item, "request_status"):
        extras.append(pytest_html.extras.text(f"Request Status: {item.request_status}", name="Request Status"))

    # --------------------------------------------------------
    # TEST DETAILS
    # --------------------------------------------------------

    if hasattr(item, "report_data"):

        data = item.report_data

        html = """
        <h2 style="font-family:Arial; color:#333;">Test Execution Details</h2>

        <table border="1" style="border-collapse:collapse; width:100%; font-family:Arial; font-size:14px;">

        <tr style="font-weight:bold;">
        <th style="padding:10px; text-align:left;">Field</th>
        <th style="padding:10px; text-align:left;">Value</th>
        </tr>
        """

        for key, value in data.items():
            html += f"""
            <tr>
            <td style="padding:10px;"><b>{key}</b></td>
            <td style="padding:10px;">{value}</td>
            </tr>
            """

        html += "</table>"

        extras.append(pytest_html.extras.html(html))

    # --------------------------------------------------------
    # SAVE EXTRAS
    # --------------------------------------------------------

    report.extras = extras


# ============================================================
# REPORT TITLE
# ============================================================

def pytest_html_report_title(report):
    report.title = "ABSA Playwright Automation Report"