import uuid
import random
import string
from playwright.sync_api import expect
from locators.user_management_locator import usermanagement_locators
from pages.common import CommonPage
from test_data.user_data import ADMIN_USER_DATA


class UserManagementPage(CommonPage):

    def __init__(self, page):
        super().__init__(page)

    # VERIFY USER MANAGEMENT PAGE
    def verify_page_opened(self):
        expect(self.page.locator(usermanagement_locators.TITLE)).to_be_visible(timeout=30000)
        print("User Management page is displayed")

    # CREATE USER
    def admincreation(self):

        # LOAD ADMIN USER TEST DATA
        name = ADMIN_USER_DATA["name"]
        city = ADMIN_USER_DATA["city"]
        country = ADMIN_USER_DATA["country"]
        category = ADMIN_USER_DATA["category"]
        state = ADMIN_USER_DATA["state"]
        authorisation_profile = ADMIN_USER_DATA["authorisation_profile"]
        security_profile = ADMIN_USER_DATA["security_profile"]

        # CREATE NEW USER
        self.click_button(usermanagement_locators.CREATE_NEW_USER)
        expect(self.page.get_by_text("Workspace", exact=True)).to_be_visible(timeout=30000)
        print("Create New User page opened")

        # WORKSPACE
        self.select_dropdown(usermanagement_locators.SELECT_WORKSPACE_ROLE, "Super Admin")
        print("Workspace selected: Super Admin")

        # PROCEED TO USER DETAILS
        self.click_button(usermanagement_locators.PROCEED_BUTTON)
        expect(self.page.get_by_text("User Details", exact=True)).to_be_visible(timeout=30000)
        print("User Details page is displayed")

        # CATEGORY
        self.select_dropdown(usermanagement_locators.SELECT_CATEGORY, category)
        print(f"Category selected: {category}")

        # EMAIL
        random_email = f"vinu_{uuid.uuid4().hex[:8]}@tecnotree.com"
        self.fill_placeholder(usermanagement_locators.EMAIL_ADDRESS, random_email)
        print(f"Email entered: {random_email}")

        # FULL NAME
        full_name_field = self.page.get_by_placeholder(usermanagement_locators.FULL_NAME, exact=True)

        expect(full_name_field).to_be_visible(timeout=30000)
        expect(full_name_field).to_be_enabled(timeout=30000)

        full_name_field.evaluate(
            """(element, value) => {
                const setter = Object.getOwnPropertyDescriptor(
                    HTMLInputElement.prototype,
                    'value'
                ).set;
                setter.call(element, value);
                element.dispatchEvent(new Event('input', { bubbles: true }));
                element.dispatchEvent(new Event('change', { bubbles: true }));
                element.dispatchEvent(new Event('blur', { bubbles: true }));
            }""",
            name
        )

        expect(full_name_field).to_have_value(name, timeout=30000)
        print(f"Full name entered: {name}")

        # PHONE
        phone_number = "07" + str(random.randint(10000000, 99999999))
        self.fill_input_safely(usermanagement_locators.PHONE_NUMBER, phone_number)
        print(f"Phone number entered: {phone_number}")

        # USERNAME
        username = "vinu" + "".join(random.choices(string.ascii_lowercase, k=8))
        self.fill_input_safely(usermanagement_locators.USER_NAME, username)
        print(f"Username entered: {username}")

        # SCROLL
        self.page.mouse.wheel(0, 600)

        # LOCATION INFORMATION
        self.fill_field(
            usermanagement_locators.LOCATION_INFORMATION,
            "VK Kampala, Central Region, Uganda"
        )
        print("Location information entered")

        # ADDRESS LINE 1
        self.fill_field(
            usermanagement_locators.ADDRESS_LINE_1,
            "Plot 12, Kampala Road, Vincent Street"
        )

        # ADDRESS LINE 2
        self.fill_field(
            usermanagement_locators.ADDRESS_LINE_2,
            "Gulu Gulu Nakasero"
        )

        # ADDRESS LINE 3
        self.fill_field(
            usermanagement_locators.ADDRESS_LINE_3,
            "Uganda"
        )

        # COMPANY DIGITAL ADDRESS
        self.fill_field(
            usermanagement_locators.COMPANY_DIGITAL_ADDRESS,
            "KLA-123-4567"
        )

        # COUNTRY
        self.select_dropdown(usermanagement_locators.SELECT_COUNTRY, country)
        print(f"Country selected: {country}")

        # STATE
        self.select_dropdown(usermanagement_locators.STATE_OF_ORIGIN, state)
        print(f"State selected: {state}")

        # CITY
        self.select_dropdown(usermanagement_locators.SELECT_CITY, city)
        print(f"City selected: {city}")

        # PO BOX
        self.fill_field(usermanagement_locators.PO_BOX, "560093")

        # LANDMARK
        self.fill_field(
            usermanagement_locators.LANDMARK,
            "Near Victoria Tower"
        )

        # PROCEED TO ATTACH PROFILES
        self.click_button(usermanagement_locators.PROCEED_BUTTON)

        expect(
            self.page.get_by_text(
                usermanagement_locators.ATTACH_PROFILES,
                exact=True
            )
        ).to_be_visible(timeout=30000)

        print("Attach Profiles page is displayed")

        # AUTHORISATION PROFILE
        authorisation_dropdown = self.page.locator(
            usermanagement_locators.SELECT_AUTHORIZATION_PROFILE
        )

        expect(authorisation_dropdown).to_be_visible(timeout=30000)
        expect(authorisation_dropdown).to_be_enabled(timeout=30000)

        authorisation_dropdown.click()

        authorisation_option = self.page.get_by_role(
            "option",
            name=authorisation_profile,
            exact=True
        )

        expect(authorisation_option).to_be_visible(timeout=30000)
        authorisation_option.click()

        print(f"Authorisation Profile selected: {authorisation_profile}")

        # SECURITY PROFILE
        security_dropdown = self.page.locator(
            usermanagement_locators.SELECT_SECURITY_PROFILE
        )

        expect(security_dropdown).to_be_visible(timeout=30000)
        expect(security_dropdown).to_be_enabled(timeout=30000)

        security_dropdown.click()

        security_option = self.page.get_by_role(
            "option",
            name=security_profile,
            exact=True
        )

        expect(security_option).to_be_visible(timeout=30000)
        security_option.click()

        print(f"Security Profile selected: {security_profile}")

        # PROCEED TO PREVIEW
        self.click_button(usermanagement_locators.PROCEED_BUTTON)

        expect(
            self.page.get_by_text(
                usermanagement_locators.PREVIEW,
                exact=True
            )
        ).to_be_visible(timeout=30000)

        print("Preview page is displayed")

        # VALIDATE CATEGORY
        category_value = (
            self.page.get_by_text("Category", exact=True)
            .locator("..")
            .locator("span")
            .nth(1)
        )

        expect(category_value).to_have_text(category, timeout=30000)
        print(f"Category validated: {category}")

        # VALIDATE COUNTRY
        country_value = (
            self.page.get_by_text("Country", exact=True)
            .locator("..")
            .locator("span")
            .nth(1)
        )

        expect(country_value).to_have_text(country, timeout=30000)
        print(f"Country validated: {country}")

        # VALIDATE STATE
        state_value = (
            self.page.get_by_text("State of Origin", exact=True)
            .locator("..")
            .locator("span")
            .nth(1)
        )

        expect(state_value).to_have_text(state, timeout=30000)
        print(f"State validated: {state}")

        # VALIDATE CITY
        city_value = (
            self.page.get_by_text("City", exact=True)
            .locator("..")
            .locator("span")
            .nth(1)
        )

        expect(city_value).to_have_text(city, timeout=30000)
        print(f"City validated: {city}")

        print("Preview details validated")

        # FINAL SUBMISSION
        self.click_button(usermanagement_locators.PROCEED_BUTTON)
        print("Final Proceed button clicked")

        # SUCCESS PAGE
        expect(
            self.page.get_by_text(
                usermanagement_locators.SUBMISSION_PENDING,
                exact=True
            )
        ).to_be_visible(timeout=30000)

        expect(
            self.page.get_by_text(
                usermanagement_locators.SUBMISSION_SUCCESS,
                exact=True
            )
        ).to_be_visible(timeout=30000)

        expect(
            self.page.get_by_text(
                usermanagement_locators.APPROVAL_PENDING,
                exact=True
            )
        ).to_be_visible(timeout=30000)

        print("New User Request Submitted Successfully")
        print("Approval Pending")

        # STATUS
        expect(
            self.page.get_by_text(
                usermanagement_locators.IN_APPROVAL,
                exact=True
            )
        ).to_be_visible(timeout=30000)

        print("Request status: In-Approval")

        # REQUEST ID
        request_id = (
            self.page.get_by_text(
                usermanagement_locators.REQUEST_ID,
                exact=True
            )
            .locator("..")
            .locator("span")
            .nth(2)
            .inner_text()
        )

        print(f"Request ID: {request_id}")

        # RETURN ACTUAL USERNAME AND REQUEST ID
        return username, request_id

    # CLICK DASHBOARD
    def click_dashboard(self):
        self.page.get_by_role("button", name="Dashboard", exact=True).click()

    # CLICK BACK OFFICE
    def click_back_office(self):
        self.page.get_by_role("button", name="Go to Back Office", exact=True).click()