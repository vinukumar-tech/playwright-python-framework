from locators.login_locator import LoginLocators

class Loginpage:

    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        print("Login method started")
        self.page.locator(LoginLocators.USERNAME).fill(username)
        print("Username value:",self.page.locator(LoginLocators.USERNAME).input_value())
        self.page.locator(LoginLocators.PASSWORD).fill(password)
        #print("Password value:",self.page.locator(LoginLocators.PASSWORD).input_value())
        self.page.locator(LoginLocators.LOGIN).click()
        print("Login button clicked")

    def click_logo(self):
        self.page.locator(LoginLocators.LOGO).click()

    def logout(self):
        self.page.locator(LoginLocators.PROFILE).click()
        self.page.locator(LoginLocators.LOGOUT).click()
        print("Logout clicked")