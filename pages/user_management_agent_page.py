from playwright.sync_api import expect
from pages.common import CommonPage
from locators.user_management_locator import usermanagement_locators
from test_data.user_data import generate_agent_data


class UserManagementAgentPage(CommonPage):

    def __init__(self, page):
        super().__init__(page)

    # VERIFY PAGE
    def verify_page_opened(self):
        title = self.page.get_by_text("User Management", exact=True).first
        expect(title).to_be_visible(timeout=30000)
        print("User Management page verified")

    # FILL BY PLACEHOLDER
    def fill_agent_placeholder(self, placeholder, value, timeout=30000, delay=3):
        field = self.page.get_by_placeholder(placeholder, exact=True)
        expect(field).to_be_visible(timeout=timeout)
        expect(field).to_be_enabled(timeout=timeout)
        value = str(value)

        for attempt in range(3):
            field.click()
            field.press("Control+A")
            field.press_sequentially(value, delay=delay)

            actual_value = field.input_value()

            if actual_value == value:
                print(f"{placeholder} entered successfully")
                return

            print(f"{placeholder} retry required. Attempt: {attempt + 1}")
            print(f"Expected: {value}")
            print(f"Actual: {actual_value}")

            field.press("Control+A")

        raise AssertionError(f"{placeholder} value not retained. Expected: {value}, Actual: {field.input_value()}")

    # SELECT CATEGORY
    def select_agent_category(self, value, timeout=30000):
        category_dropdown = self.page.locator("#mui-component-select-category")
        expect(category_dropdown).to_be_visible(timeout=timeout)
        category_dropdown.click()
        option = self.page.get_by_role("option", name=value, exact=True)
        expect(option).to_be_visible(timeout=timeout)
        option.click()
        expect(category_dropdown).to_contain_text(value, timeout=timeout)
        print("Category selected:", value)

    # AGENT CREATION
    def agentcreation(self):
        agent_data = generate_agent_data()
        print("Agent data generated:", agent_data)

        # CREATE NEW USER
        self.click_button(usermanagement_locators.CREATE_NEW_USER)
        print("Create New User clicked")

        # WORKSPACE
        self.select_dropdown(usermanagement_locators.SELECT_WORKSPACE_ROLE, agent_data["workspace"])
        print("Workspace selected:", agent_data["workspace"])

        # PROCEED
        self.page.get_by_test_id(usermanagement_locators.PROCEED_ICON).click()
        print("Proceed icon clicked")

        # USER DETAILS
        expect(self.page.get_by_text("User Details", exact=True)).to_be_visible(timeout=30000)
        print("User Details page opened")

        # AGENT CODE
        agent_code_field = self.page.get_by_placeholder("Enter Agent Code", exact=True)
        expect(agent_code_field).to_be_visible(timeout=30000)
        expect(agent_code_field).not_to_have_value("", timeout=10000)
        agent_code = agent_code_field.input_value()
        print("Agent Code:", agent_code)

        # AGENT CODE ALIAS
        self.fill_agent_placeholder("Enter Agent Code Alias", agent_data["agent_code_alias"])
        print("Agent Code Alias entered")

        # TIN
        self.fill_agent_placeholder("Enter TIN", agent_data["tin"])
        print("TIN entered")

        # FLOAT ACCOUNT NUMBER
        self.fill_agent_placeholder("Enter Float Account Number", agent_data["float_account_number"])
        print("Float Account Number entered")

        # BUSINESS NAME
        business_name_field = self.page.get_by_placeholder("Enter Business Name", exact=True)
        expect(business_name_field).to_be_visible(timeout=30000)
        business_name = business_name_field.input_value()
        print("Business Name:", business_name)

        # BUSINESS OWNER
        self.fill_agent_placeholder("Enter Business Owner", agent_data["business_owner"])
        print("Business Owner entered")

        # NATURE OF BUSINESS
        self.fill_agent_placeholder("Enter Nature of Business", agent_data["nature_of_business"])
        print("Nature of Business entered")

        # PHONE NUMBER
        self.fill_agent_placeholder("Enter Phone Number", agent_data["phone_number"])
        print("Phone Number entered")

        # EMAIL
        self.fill_agent_placeholder("Enter Email Address", agent_data["email"], delay=5)
        print("Email entered")

        # COMMISSION ACCOUNT NUMBER
        self.fill_agent_placeholder("Enter Commission Account Number", agent_data["commission_account_number"], delay=10)
        print("Commission Account Number entered")

        # TERMINAL ID
        self.fill_agent_placeholder("Enter Terminal ID", agent_data["terminal_id"])
        print("Terminal ID entered")

        # ACTUAL LOCATION
        self.fill_agent_placeholder("Enter Actual Location", agent_data["actual_location"])
        print("Actual Location entered")

        # GPS COORDINATES
        self.fill_agent_placeholder("Enter GPS Coordinates", agent_data["coordinates"])
        print("GPS Coordinates entered:", agent_data["coordinates"])

        # DISTRICT
        self.fill_agent_placeholder("Enter District", agent_data["district"])
        print("District entered")

        # PARENT REGION
        self.fill_agent_placeholder("Enter Parent Region", agent_data["parent_region"])
        print("Parent Region entered")

        # PARENT BRANCH
        self.fill_agent_placeholder("Enter Parent Branch", agent_data["parent_branch"])
        print("Parent Branch entered")

        # MTN POS SIMCARD
        self.fill_agent_placeholder("Enter MTN POS SimCard", agent_data["mtn_pos_simcard"])
        print("MTN POS SimCard entered")

        # AIRTEL POS SIMCARD
        self.fill_agent_placeholder("Enter Airtel POS SimCard", agent_data["airtel_pos_simcard"])
        print("Airtel POS SimCard entered")

        # CATEGORY
        self.select_agent_category(agent_data["category"])
        print("Category selected:", agent_data["category"])

        # PROCEED TO ATTACH PROFILES
        self.click_button(usermanagement_locators.PROCEED_BUTTON)
        print("Proceed to Attach Profiles clicked")

        # ATTACH PROFILES
        expect(self.page.get_by_text(usermanagement_locators.ATTACH_PROFILES, exact=True)).to_be_visible(timeout=30000)
        print("Attach Profiles page opened")

        # AUTHORIZATION PROFILE
        auth_dropdown = self.page.locator(usermanagement_locators.SELECT_AUTHORIZATION_PROFILE)
        expect(auth_dropdown).to_be_visible(timeout=30000)
        expect(auth_dropdown).to_be_enabled(timeout=30000)
        auth_dropdown.click()

        auth_option = self.page.get_by_role("option", name=agent_data["authorisation_profile"], exact=True)
        expect(auth_option).to_be_visible(timeout=30000)
        auth_option.click()
        print("Authorization Profile selected:", agent_data["authorisation_profile"])

        # SECURITY PROFILE
        security_dropdown = self.page.locator(usermanagement_locators.SELECT_SECURITY_PROFILE)
        expect(security_dropdown).to_be_visible(timeout=30000)
        expect(security_dropdown).to_be_enabled(timeout=30000)
        security_dropdown.click()

        security_option = self.page.get_by_role("option", name=agent_data["security_profile"], exact=True)
        expect(security_option).to_be_visible(timeout=30000)
        security_option.click()
        print("Security Profile selected:", agent_data["security_profile"])

        # PROCEED TO PREVIEW
        self.click_button(usermanagement_locators.PROCEED_BUTTON)
        print("Proceed to Preview clicked")

        # VERIFY PREVIEW
        expect(self.page.get_by_text("Preview", exact=True)).to_be_visible(timeout=30000)
        print("Preview page opened")

        # VALIDATE PREVIEW DETAILS
        expect(self.page.get_by_text("Workspace", exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text("Agent", exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text("NormalAgent", exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_code, exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["agent_code_alias"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["tin"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["float_account_number"], exact=True)).to_be_visible(timeout=30000)

        # BUSINESS NAME
        business_name_label = self.page.get_by_text("Business Name", exact=True)
        expect(business_name_label).to_be_visible(timeout=30000)
        business_name_value = business_name_label.locator("xpath=following::*[1]").inner_text()
        assert business_name_value.strip() != "", "Business Name is empty in Preview"
        print("Business Name validated:", business_name_value)

        expect(self.page.get_by_text(agent_data["business_owner"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["nature_of_business"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["phone_number"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["email"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["commission_account_number"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["terminal_id"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["actual_location"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["coordinates"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["district"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["parent_region"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["parent_branch"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["mtn_pos_simcard"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["airtel_pos_simcard"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["authorisation_profile"], exact=True)).to_be_visible(timeout=30000)
        expect(self.page.get_by_text(agent_data["security_profile"], exact=True)).to_be_visible(timeout=30000)

        print("All Preview details validated successfully")

        # PROCEED FROM PREVIEW
        proceed_button = self.page.get_by_role("button", name="Proceed", exact=True)
        expect(proceed_button).to_be_visible(timeout=30000)
        expect(proceed_button).to_be_enabled(timeout=30000)
        proceed_button.click()
        print("Proceed from Preview clicked")

        # VERIFY SUBMISSION
        expect(self.page.get_by_text(usermanagement_locators.SUBMISSION_SUCCESS, exact=True)).to_be_visible(timeout=60000)
        print("Agent creation success message displayed")

        # REQUEST ID
        request_id_label = self.page.get_by_text("Request ID", exact=True)
        expect(request_id_label).to_be_visible(timeout=30000)
        request_id_row = request_id_label.locator("xpath=..")
        request_id = request_id_row.locator("span").nth(2).inner_text()
        print("Request ID:", request_id)

        # REQUEST STATUS
        status_label = self.page.get_by_text("Status", exact=True)
        expect(status_label).to_be_visible(timeout=30000)
        status_row = status_label.locator("xpath=..")
        request_status = status_row.locator("span").nth(2).inner_text()
        print("Request Status:", request_status)

        # GO TO BACK OFFICE
        back_office_button = self.page.get_by_role("button", name="Go to Back Office", exact=True)
        expect(back_office_button).to_be_visible(timeout=30000)
        expect(back_office_button).to_be_enabled(timeout=30000)
        back_office_button.click()
        print("Go to Back Office clicked")
        self.page.wait_for_timeout(2000)
        print("Back Office opened")

        return {
            "agent_code": agent_code,
            "agent_code_alias": agent_data["agent_code_alias"],
            "tin": agent_data["tin"],
            "float_account_number": agent_data["float_account_number"],
            "business_name": business_name_value,
            "business_owner": agent_data["business_owner"],
            "nature_of_business": agent_data["nature_of_business"],
            "phone_number": agent_data["phone_number"],
            "email": agent_data["email"],
            "commission_account_number": agent_data["commission_account_number"],
            "terminal_id": agent_data["terminal_id"],
            "actual_location": agent_data["actual_location"],
            "coordinates": agent_data["coordinates"],
            "district": agent_data["district"],
            "parent_region": agent_data["parent_region"],
            "parent_branch": agent_data["parent_branch"],
            "mtn_pos_simcard": agent_data["mtn_pos_simcard"],
            "airtel_pos_simcard": agent_data["airtel_pos_simcard"],
            "category": agent_data["category"],
            "authorisation_profile": agent_data["authorisation_profile"],
            "security_profile": agent_data["security_profile"],
            "request_id": request_id,
            "request_status": request_status
        }

    # CLICK BACK OFFICE
    def click_back_office(self):
        self.page.get_by_role("button", name="Go to Back Office", exact=True).click()