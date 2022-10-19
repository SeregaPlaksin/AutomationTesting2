import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pom.index_page import IndexPage, AuthPage
from pom.main_page import MainButton, Sorted
import time


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture(scope='function')
def setup(get_webdriver):
    driver = get_webdriver
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def setup_auth(get_webdriver):
    driver = get_webdriver
    url = 'https://www.saucedemo.com/'
    driver.get(url)
    auth_page = AuthPage(driver)
    auth_page.enter_correct_username()
    auth_page.enter_correct_password()
    auth_page.click_login_button()

    yield driver
    driver.quit()


@pytest.fixture
def auth_page(setup):
    yield AuthPage(setup)


@pytest.fixture
def main_page(setup_auth):
    yield MainButton(setup_auth)


@pytest.fixture
def sort_page(setup_auth):
    yield Sorted(setup_auth)


@pytest.fixture
def auth_page_input_data(setup_auth):
    yield AuthPage(setup_auth)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    marker = item.get_closest_marker("ui")
    if marker:
        if rep.when == "call" and rep.failed:
            try:
                allure.attach(item.instance.driver.get_screenshot_as_png(),
                              name=item.name,
                              attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(e)
