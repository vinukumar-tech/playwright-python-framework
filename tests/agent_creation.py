import pytest
from pages.approval_page import ApprovalPage
from pages.login_page import Loginpage
from pages.dashboard_page import DashboardPage
from pages.user_management_agent_page import UserManagementAgentPage
from utils.excel_utils import save_test_result


Base_URL = "https://diwa-sit.tecnotree.com/diwa-web-ui/"
USERNAME = "diwaMasterUser"
PASSWORD = "Tecnotree#5"


def test_agent_creation(page):

    # OPEN APPLICATION
    page.goto(
        Base_URL,
        wait_until="domcontentloaded",
        timeout=60000
    )

    print("Application opened")
    print("URL:", page.url)
    print("TITLE:", page.title())

    # LOGIN
    login = Loginpage(page)
    login.login(
        USERNAME,
        PASSWORD
    )

    print("Login completed")

    # DASHBOARD
    dashboard = DashboardPage(page)
    dashboard.verify_home_page_opened()

    print("Home page is displayed")

    menu_values = dashboard.left_menu()

    print(
        "Values received in test:",
        menu_values
    )

    assert "User Management" in menu_values

    # OPEN USER MANAGEMENT
    dashboard.click_user_management()

    print("User Management opened")

    # AGENT CREATION
    agent = UserManagementAgentPage(page)

    agent.verify_page_opened()

    agent_data = agent.agentcreation()

    print("Agent creation completed")
    print(
        "Agent Code:",
        agent_data["agent_code"]
    )

    print(
        "Business Name:",
        agent_data["business_name"]
    )

    print(
        "Request ID:",
        agent_data["request_id"]
    )

    print(
        "Request Status:",
        agent_data["request_status"]
    )

    # SAVE AGENT RESULT TO EXCEL
    save_test_result({
        "Test Case": "Agent Creation",
        "Application": "DIWA",
        "Environment": "SIT",
        "Browser": "Chromium",
        "Agent Code": agent_data["agent_code"],
        "Agent Code Alias": agent_data["agent_code_alias"],
        "TIN": agent_data["tin"],
        "Float Account Number": agent_data["float_account_number"],
        "Business Name": agent_data["business_name"],
        "Business Owner": agent_data["business_owner"],
        "Nature of Business": agent_data["nature_of_business"],
        "Phone": agent_data["phone_number"],
        "Email": agent_data["email"],
        "Commission Account Number": agent_data["commission_account_number"],
        "Terminal ID": agent_data["terminal_id"],
        "Actual Location": agent_data["actual_location"],
        "GPS Coordinates": agent_data["coordinates"],
        "District": agent_data["district"],
        "Parent Region": agent_data["parent_region"],
        "Parent Branch": agent_data["parent_branch"],
        "MTN POS SimCard": agent_data["mtn_pos_simcard"],
        "Airtel POS SimCard": agent_data["airtel_pos_simcard"],
        "Category": "NormalAgent",
        "Authorisation Profile": "AUTH_PRO_DEMO_NEW",
        "Security Profile": "Security_Profile_Demo_New",
        "Request ID": agent_data["request_id"],
        "Request Status": agent_data["request_status"],
        "Overall Result": "PASSED"
    }, sheet_name="Agent Creation")

    print(
        "Agent execution saved to Agent Creation sheet"
    )

    # APPROVAL
    approval = ApprovalPage(page)

    approval.approve_request(
        table_name="User Management",
        request_id=agent_data["request_id"],
        tab="Agent",
        comments="Approved through automation"
    )

    print("Agent approval completed")

    # LOGOUT
    login.click_logo()

    login.logout()

    print("Logout completed")