import pytest
from datetime import datetime
from pages.approval_page import ApprovalPage
from test_data.user_data import ADMIN_USER_DATA
from utils.excel_utils import save_test_result
from pages.login_page import Loginpage
from pages.dashboard_page import DashboardPage
from pages.user_management_page import UserManagementPage
from utils.report_utils import take_screenshot

Base_URL = "https://diwa-sit.tecnotree.com/diwa-web-ui/"
USERNAME = "diwaMasterUser"
PASSWORD = "Tecnotree#5"


def test_valid_login(page, request):

    # REPORT DATA
    report_data = {}
    request.node.report_data = report_data

    # OPEN APPLICATION
    page.goto(Base_URL, wait_until="domcontentloaded", timeout=60000)
    print("URL:", page.url)
    print("TITLE:", page.title())
    report_data["Test Case"] = "Admin User Creation"
    report_data["Application"] = "DIWA"
    report_data["Environment"] = "SIT"
    report_data["Browser"] = "Chromium"
    report_data["Application URL"] = Base_URL
    take_screenshot(page, "01_application")

    # LOGIN
    print("Login method started")
    login = Loginpage(page)
    login.login(USERNAME, PASSWORD)
    print("Login completed")
    report_data["Login"] = "PASSED"
    take_screenshot(page, "02_login_success")

    # VERIFY DASHBOARD
    dashboard = DashboardPage(page)
    dashboard.verify_home_page_opened()
    print("Home page is displayed")
    report_data["Dashboard"] = "PASSED"

    # VERIFY LEFT MENU
    menu_values = dashboard.left_menu()
    print("Values received in test:", menu_values)
    assert "User Management" in menu_values
    report_data["Left Menu"] = ", ".join(menu_values)

    # OPEN USER MANAGEMENT
    dashboard.click_user_management()
    user_management = UserManagementPage(page)
    user_management.verify_page_opened()
    print("User Management page is displayed")
    report_data["User Management"] = "PASSED"
    take_screenshot(page, "03_user_management")

    # ADMIN USER CREATION
    username, request_id = user_management.admincreation()
    print(f"Captured Username: {username}")
    print(f"Captured Request ID: {request_id}")

    request.node.username = username
    request.node.request_id = request_id

    report_data["Username"] = username
    report_data["Request ID"] = request_id

    # REQUEST STATUS
    request_status = "In-Approval"
    print(f"Request Status: {request_status}")

    request.node.request_status = request_status
    report_data["Request Status"] = request_status

    # USER DETAILS
    report_data["Full Name"] = ADMIN_USER_DATA["name"]
    report_data["Category"] = ADMIN_USER_DATA["category"]
    report_data["Country"] = ADMIN_USER_DATA["country"]
    report_data["State"] = ADMIN_USER_DATA["state"]
    report_data["City"] = ADMIN_USER_DATA["city"]
    report_data["Authorisation Profile"] = ADMIN_USER_DATA["authorisation_profile"]
    report_data["Security Profile"] = ADMIN_USER_DATA["security_profile"]

    # USER CREATION SCREENSHOT
    take_screenshot(page, "04_user_creation_success")

    # OVERALL RESULT
    report_data["Overall Result"] = "PASSED"

    # SAVE TEST RESULT TO EXCEL
    excel_data = {
        "Test Case": "Admin User Creation",
        "Application": "DIWA",
        "Environment": "SIT",
        "Browser": "Chromium",
        "Request ID": request_id,
        "Request Status": request_status,
        "Username": username,
        "Full Name": ADMIN_USER_DATA["name"],
        "Category": ADMIN_USER_DATA["category"],
        "Country": ADMIN_USER_DATA["country"],
        "State": ADMIN_USER_DATA["state"],
        "City": ADMIN_USER_DATA["city"],
        "Authorisation Profile": ADMIN_USER_DATA["authorisation_profile"],
        "Security Profile": ADMIN_USER_DATA["security_profile"],
        "Overall Result": "PASSED",
        "Execution Date/Time": datetime.now().strftime("%d-%b-%Y %H:%M:%S")
    }

    save_test_result(excel_data)

    # SUCCESS MESSAGE
    print("New User Request Submitted Successfully")
    print("Request status:", request_status)
    print("Request ID:", request_id)

    # GO TO BACK OFFICE
    user_management.click_back_office()
    print("Go to Back Office clicked")

    # APPROVAL
    approval = ApprovalPage(page)
    approval.approve_request(table_name="User Management", request_id=request_id, tab="Admin", comments="Approved through automation")

    print("Admin approval completed")

    # LOGOUT
    page.wait_for_timeout(5000)
    login.click_logo()
    login.logout()
    print("Logout completed")

    report_data["Logout"] = "PASSED"