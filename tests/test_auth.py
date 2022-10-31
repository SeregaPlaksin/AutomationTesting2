import pytest
import allure

from conftest import main_page


@allure.story('Assertion test cases')
class TestOne:
    def test_1(self):
        assert 1 == 1

    def test_2(self):
        assert 2 == 2

    def test_3(self):
        assert 3 == 3


logins = ('locked_out_user',
          'problem_user',
          'performance_glitch_user')


@allure.label("owner", "Sergey!!")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description('Checking successful login')
@pytest.mark.ui
@pytest.mark.parametrize('login', logins)
def test_successful_login(auth_page, login):
    with allure.step('input correct username'):
        auth_page.enter_correct_username(login)
    with allure.step('input correct password'):
        auth_page.enter_correct_password()
    with allure.step('click login'):
        auth_page.click_login_button()
    with allure.step('check successful login'):
        auth_page.successful_login()


@pytest.mark.api
def test_unsuccessful_login(auth_page):
    auth_page.enter_uncorrected_username()
    auth_page.enter_correct_password()
    auth_page.click_login_button()
    auth_page.unsuccessful_login()


@pytest.mark.smoke
def test_logout(auth_page_input_data, main_page):
    main_page.click_main_button()
    auth_page_input_data.click_logout_button()
    auth_page_input_data.visible_login_button()
