import pytest

from base_object.base import BaseObject
from base_object.helper import Helper
from base_object.locators import Locators
import  json
import os


path = os.path.dirname(os.path.realpath(__file__))
path2 = str(path)+'\\passwords.json'
file = open(path2, 'rb')
my_passwords = json.load(file)
password = my_passwords['password']
username = my_passwords['username']



class AuthPage(BaseObject, Helper):

    def enter_correct_username(self, data='standard_user'):
        self.to_input('css', Locators.LOGIN, data)

<<<<<<< HEAD
class AuthPage(BaseObject, Helper):

    def enter_correct_username(self):
        self.to_input('css', Locators.LOGIN, username)

    def enter_uncorrect_username(self):
=======
    def enter_uncorrected_username(self):
>>>>>>> 5016f3a (update)
        self.to_input('css', Locators.LOGIN, '123qwe')

    def enter_correct_password(self):
        self.to_input('css', Locators.PASS, password)

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
