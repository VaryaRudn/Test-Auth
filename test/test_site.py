from pages.loginpage import LoginPage
from pages.productspage import ProductPage

import allure

@allure.feature('Login')
def test_login(browser):
    loginpage = LoginPage(browser)
    loginpage.open()
    loginpage.send_login()
    loginpage.send_password()
    loginpage.login_button()

    productpage = ProductPage(browser)
    productpage.check_header()

@allure.feature('Logout')
def test_logout(browser):
    loginpage = LoginPage(browser)
    loginpage.open()
    loginpage.send_login()
    loginpage.send_password()
    loginpage.login_button()

    productpage = ProductPage(browser)
    productpage.start_logout()

    loginpage_after_logout = LoginPage(browser)
    loginpage_after_logout.logout_info()