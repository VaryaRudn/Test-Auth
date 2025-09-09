from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.saucedemo.com/')

    def send_login(self):
        login_space = self.browser.find_element(By.CSS_SELECTOR, '#user-name')
        login_space.send_keys('standard_user')

    def send_password(self):
        password_link = self.browser.find_element(By.CSS_SELECTOR, "#password")
        password_link.send_keys("secret_sauce")

    def login_button(self):
        login_button_link = self.browser.find_element(By.CSS_SELECTOR, '#login-button')
        login_button_link.click()

    def logout_info(self):
        login_info = self.browser.find_element(By.CSS_SELECTOR, '#root > div > div.login_logo')
        return login_info.is_displayed()