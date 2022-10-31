from base_object.base import BaseObject
from base_object.helper import Helper
from base_object.locators import Locators


class AuthPage(BaseObject, Helper):

    def enter_correct_username(self, data='standard_user'):
        self.to_input('css', Locators.LOGIN, data)

    def enter_uncorrected_username(self):
        self.to_input('css', Locators.LOGIN, '123qwe')

    def enter_correct_password(self):
        self.to_input('css', Locators.PASS, 'secret_sauce')

    def click_login_button(self):
        self.to_click('css', Locators.LOGIN_BUTTON)

    def click_logout_button(self):
        self.to_click('css', Locators.LOGOUT)

    def visible_login_button(self):
        expected_text = 'Login'
        actual_text = self.to_get_attribute('css', Locators.LOGIN_BUTTON, 'value')
        self.equal(expected_text, actual_text)

    def successful_login(self):
        expected_text = 'PRODUCTS'
        actual_text = self.to_text('css', Locators.TITLE)
        self.equal(expected_text, actual_text)

    def unsuccessful_login(self):
        expected_text = 'Epic sadface: Username and password do not match any user in this service'
        actual_text = self.to_text('css', Locators.ERROR_MESSAGE)
        self.equal(expected_text, actual_text)
