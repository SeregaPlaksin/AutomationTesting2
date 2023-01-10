from base_object.base import BaseObject
from base_object.locators import LocatorsCart, LocatorsMain
from base_object.helper import Helper
import random


class ShoppingCart(BaseObject, Helper):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_shopping_cart(self):
        self.to_click('css', LocatorsCart.SHOPPING_CART)

    def checkout_shopping_cart(self):
        expected_text = 'CHECKOUT: YOUR INFORMATION'
        actual_text = self.to_text('css', LocatorsMain.TITLE)
        self.equal(expected_text, actual_text)

    def open_shopping_cart(self):
        expected_text = 'YOUR CART'
        actual_text = self.to_text('css', LocatorsMain.TITLE)
        self.equal(expected_text, actual_text)

    def checkout_shopping_cart_badge(self):
        expected_text = '1'
        actual_text = self.to_text('css', LocatorsCart.SHOPPING_CART_BADGE)
        self.equal(expected_text, actual_text)

    def click_random_inventory_element(self):
        elements = self.are_visible('css', LocatorsCart.SHOPPING_CART_INVENTORY, LocatorsCart.SHOPPING_CART_INVENTORY)
        random_element = (elements[random.randint(0, len(elements) - 1)])
        global text_element
        text_element = random_element.text
        random_element.click()
        return text_element

    def checkout_shopping_cart_inventory(self):
        expected_text = text_element
        actual_text = self.to_text('css', LocatorsCart.SHOPPING_CART_INVENTORY2)
        self.equal(expected_text, actual_text)

    def click_add_to_cart(self):
        self.to_click('css', LocatorsCart.ADD_TO_CARD)
