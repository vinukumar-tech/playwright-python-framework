from locators.dashboard_locator import dashboard_locators
from playwright.sync_api import expect


class DashboardPage:

    def __init__(self,page):
        self.page = page

    def verify_home_page_opened(self):
        expect(self.page.get_by_role("button",name=dashboard_locators.HOME)).to_be_visible(timeout=30000)
        print("Home page is displayed")

    def left_menu(self):
        menu_items=self.page.locator(dashboard_locators.LEFT_MENU_ITEMS)
        values=menu_items.all_text_contents()
        print("Left menu:" ,values)
        return values
        
    def click_user_management(self):
        self.page.get_by_role("button",name="User Management").click()




