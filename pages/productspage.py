from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, browser):
        self.browser = browser

    def check_header(self):
        header = self.browser.find_element(By.CSS_SELECTOR,'#header_container > div.header_secondary_container > span')
        assert header.text == 'Products'

    def start_logout(self):
        additional = self.browser.find_element(By.CSS_SELECTOR, '#react-burger-menu-btn')
        additional.click()
        logout_button = self.browser.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
        logout_button.click()
