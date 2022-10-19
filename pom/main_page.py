from base_object.base import BaseObject
from base_object.locators import Locators
from base_object.helper import Helper


class MainButton(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_main_button(self):
        self.to_click('css', Locators.BUTTON_MENU)

    def click_all_items(self):
        self.to_click('css', Locators.BUTTON_MENU_ALL_ITEMS)


class Basket(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_basket(self):
        self.to_click('css', Locators.BASKET)

    def checkout_basket(self):
        expected_text = 'CHECKOUT: YOUR INFORMATION'
        actual_text = self.to_text('css', Locators.TITLE)
        self.equal(expected_text, actual_text)

    def open_basket(self):
        expected_text = 'YOUR CART'
        actual_text = self.to_text('css', Locators.TITLE)
        self.equal(expected_text, actual_text)


class Sorted(BaseObject, Helper):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_dropdown_price_lth(self):
        self.select_dropdown('css', Locators.SORT_CONTAINER, 'Price (low to high)')

    def sort_by_price_lth(self):
        price_object = self.are_visible('css', Locators.INVENTORY_PRICE, Locators.INVENTORY_PRICE)
        return self.generation_list(price_object)

    def sort_by_price_lists(self):
        actual_list = self.sort_by_price_lth()
        expected_list = list(actual_list)
        self.equal(actual_list, expected_list)






