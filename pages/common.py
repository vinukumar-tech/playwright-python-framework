from dataclasses import field
from socket import timeout

from playwright.sync_api import expect


class CommonPage:

    def __init__(self, page):
        self.page = page

    # ==========================================================
    # WAIT FOR PAGE ELEMENT
    # ==========================================================

    def wait_for_element(self, locator, timeout=30000):
        expect(locator).to_be_visible(timeout=timeout)
        expect(locator).to_be_enabled(timeout=timeout)
        return locator

    # ==========================================================
    # CLICK BUTTON
    # ==========================================================

    def click_button(self, button_name, timeout=30000):

        button = self.page.get_by_role(
            "button",
            name=button_name,
            exact=True
        )

        self.wait_for_element(button, timeout)

        button.click()

    # ==========================================================
    # FILL NORMAL INPUT
    # ==========================================================

    def fill_field(self, locator, value, timeout=30000):

        field = self.page.locator(locator)

        self.wait_for_element(field, timeout)

        field.fill(value)

        # Verify application actually retained the value
        expect(field).to_have_value(
            value,
            timeout=timeout
        )

    # ==========================================================
    # FILL PLACEHOLDER INPUT
    # ==========================================================

    def fill_placeholder(self, placeholder, value, timeout=30000):

        field = self.page.get_by_placeholder(
            placeholder,
            exact=True
        )

        self.wait_for_element(field, timeout)

        field.fill(value)

        expect(field).to_have_value(
            value,
            timeout=timeout
        )

    # ==========================================================
    # FILL FULL NAME
    # Special handling for this application's React field
    # ==========================================================

    def fill_text_slowly(self, locator, value, timeout=30000):

        field = self.page.locator(locator)

        self.wait_for_element(field, timeout)

        field.click()

        field.press_sequentially(
            value,
            delay=100
        )

        field.press("Tab")

        expect(field).to_have_value(
            value,
            timeout=timeout
        )

    # ==========================================================
    # SELECT DROPDOWN
    # ==========================================================

    def select_dropdown(
        self,
        dropdown_name,
        required_value,
        timeout=30000
    ):

        dropdown = self.page.get_by_role(
            "combobox",
            name=dropdown_name,
            exact=True
        )

        expect(
            dropdown
        ).to_be_visible(timeout=timeout)

        expect(
            dropdown
        ).to_be_enabled(timeout=timeout)

        dropdown.click()

        option = self.page.get_by_role(
            "option",
            name=required_value,
            exact=True
        )

        expect(
            option
        ).to_be_visible(timeout=timeout)

        expect(
            option
        ).to_be_enabled(timeout=timeout)

        option.click()

        print(
            f"Selected value: {required_value}"
        )



    def fill_input_safely(self, locator, value, timeout=30000):
        field = self.page.locator(locator)

        self.wait_for_element(field, timeout)

        field.click()

        field.evaluate(
        """(element, value) => {
        const setter = Object.getOwnPropertyDescriptor(
        HTMLInputElement.prototype,
        'value'
        ).set;

        setter.call(element, value);

        element.dispatchEvent(            new Event('input', { bubbles: true })
        );
        element.dispatchEvent(
        new Event('change', { bubbles: true })
        );

        element.dispatchEvent(
        new Event('blur', { bubbles: true })
        );
        }""",
        value
        )

        expect(field).to_have_value(value, timeout=timeout)