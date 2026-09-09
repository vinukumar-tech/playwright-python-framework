from playwright.sync_api import expect
from pages.common import CommonPage
from locators.approval_locators import approval_locators


class ApprovalPage(CommonPage):

    def __init__(self, page):
        super().__init__(page)

    # GET APPROVAL CARD
    def get_approval_card(self, table_name):

        if table_name == "User Management":

            table_title = self.page.locator(
                "span.sc-pVUti",
                has_text=table_name
            ).filter(
                has=self.page.locator("xpath=.")
            )

            table_title = self.page.locator(
                "span.sc-pVUti",
                has_text=table_name
            ).nth(0)

        else:

            table_title = self.page.get_by_text(
                table_name,
                exact=True
            ).last

        expect(table_title).to_be_visible(timeout=30000)

        table_card = table_title.locator(
            "xpath=ancestor::div[contains(@class,'sc-iAKZmh')][1]"
        )

        expect(table_card).to_be_visible(timeout=30000)

        print("Approval card found:", table_name)

        return table_card

    # GET APPROVAL TABLE
    def get_approval_table(self, table_name):

        card = self.get_approval_card(table_name)

        table = card.locator(
            "div.MuiTableContainer-root"
        )

        expect(table).to_be_visible(timeout=30000)

        return table

    # VERIFY APPROVAL TABLE
    def verify_approval_table(self, table_name):

        table = self.get_approval_table(table_name)

        expect(table).to_be_visible(timeout=30000)

        print("Approval table opened:", table_name)

        return table

    # SELECT APPROVAL TAB
    def select_tab(self, table_name, tab):

        card = self.get_approval_card(table_name)

        tab_button = card.get_by_role(
            "button",
            name=tab,
            exact=True
        )

        expect(tab_button).to_be_visible(timeout=30000)
        expect(tab_button).to_be_enabled(timeout=30000)

        tab_button.click()

        print("Selected approval tab:", tab)

        self.page.wait_for_timeout(1000)

    # SEARCH REQUEST
    def search_request(self, table_name, request_id):

        card = self.get_approval_card(table_name)

        search_by = card.get_by_role(
            "combobox",
            name=approval_locators.SEARCH_BY,
            exact=True
        )

        expect(search_by).to_be_visible(timeout=30000)
        expect(search_by).to_be_enabled(timeout=30000)

        search_by.click()

        self.page.wait_for_timeout(500)

        id_option = self.page.get_by_role(
            "option",
            name="Request ID",
            exact=True
        )

        expect(id_option).to_be_visible(timeout=30000)
        expect(id_option).to_be_enabled(timeout=30000)

        id_option.click()

        print("Search By selected: Request ID")

        search_field = card.get_by_placeholder(
            approval_locators.SEARCH_INPUT,
            exact=True
        )

        expect(search_field).to_be_visible(timeout=30000)
        expect(search_field).to_be_enabled(timeout=30000)

        search_field.fill(request_id)

        expect(search_field).to_have_value(
            request_id,
            timeout=30000
        )

        print("Request ID entered:", request_id)

        search_button = card.locator(
            "button:has(svg[data-testid='SearchIcon'])"
        )

        expect(search_button).to_be_visible(timeout=30000)
        expect(search_button).to_be_enabled(timeout=30000)

        search_button.click()

        print("Request searched:", request_id)

        self.page.wait_for_timeout(2000)

    # GET REQUEST ROW
    def get_request_row(self, table_name, request_id):

        table = self.get_approval_table(table_name)

        request_cell = table.get_by_text(
            request_id,
            exact=True
        )

        expect(request_cell).to_be_visible(timeout=30000)

        request_row = request_cell.locator(
            "xpath=ancestor::tr"
        )

        expect(request_row).to_be_visible(timeout=30000)

        print("Request found:", request_id)

        return request_row

    # APPROVE REQUEST
    def approve_request(
        self,
        table_name,
        request_id,
        tab=None,
        comments="Approved through automation"
    ):

        # VERIFY APPROVAL TABLE
        self.verify_approval_table(table_name)

        # SELECT TAB
        if tab:

            self.select_tab(
                table_name,
                tab
            )

        # SEARCH REQUEST
        self.search_request(
            table_name,
            request_id
        )

        # FIND REQUEST
        request_row = self.get_request_row(
            table_name,
            request_id
        )

        # APPROVE
        approve_button = request_row.get_by_role(
            "button",
            name=approval_locators.APPROVE_BUTTON,
            exact=True
        )

        expect(approve_button).to_be_visible(timeout=30000)
        expect(approve_button).to_be_enabled(timeout=30000)

        approve_button.click()

        print("Approve clicked")

        # CONFIRMATION
        confirmation = self.page.get_by_role(
            "heading",
            name="Confirmation",
            exact=True
        )

        expect(confirmation).to_be_visible(timeout=30000)

        print("Approval confirmation popup opened")

        # COMMENTS
        comments_field = self.page.locator(
            approval_locators.COMMENTS
        )

        expect(comments_field).to_be_visible(timeout=30000)
        expect(comments_field).to_be_enabled(timeout=30000)

        comments_field.fill(comments)

        expect(comments_field).to_have_value(
            comments,
            timeout=30000
        )

        print("Approval comment entered")

        # SUBMIT
        submit_button = self.page.locator(
            approval_locators.SUBMIT_BUTTON
        )

        expect(submit_button).to_be_visible(timeout=30000)
        expect(submit_button).to_be_enabled(timeout=30000)

        submit_button.click()

        print("Approval submitted")

        expect(confirmation).not_to_be_visible(
            timeout=30000
        )

        print("Approval completed successfully")