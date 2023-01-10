import random

from base_object.base import BaseObject
from base_object.locators import LocatorsMain
from base_object.helper import Helper


class MainPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def click_main_button(self):
        self.to_click('css', LocatorsMain.BUTTON_MENU)

    def click_all_items(self):
        self.to_click('css', LocatorsMain.BUTTON_MENU_ALL_ITEMS)







