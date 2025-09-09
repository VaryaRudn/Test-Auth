import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    print("Выберите браузер, chrome, edge или firefox")
    driver = input().lower()
    if driver == 'chrome':
        browser = webdriver.Chrome()
    elif driver == 'edge':
        browser = webdriver.Edge()
    elif driver == 'firefox':
        browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.close()