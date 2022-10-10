from base_object.base import BaseObject
from base_object.locators import Locators


class AuthPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

