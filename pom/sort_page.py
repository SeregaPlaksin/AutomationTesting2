from base_object.base import BaseObject
from base_object.locators import LocatorsSort
from base_object.helper import Helper
from natsort import natsorted


class SortedPrice(BaseObject, Helper):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_dropdown_price_lth(self):
        self.select_dropdown('css', LocatorsSort.SORT_CONTAINER, 'Price (low to high)')

    def click_dropdown_price_htl(self):
        self.select_dropdown('css', LocatorsSort.SORT_CONTAINER, 'Price (high to low)')

    def click_dropdown_name_az(self):
        self.select_dropdown('css', LocatorsSort.SORT_CONTAINER, 'Name (A to Z)')

    def click_dropdown_name_za(self):
        self.select_dropdown('css', LocatorsSort.SORT_CONTAINER, 'Name (Z to A)')

    def save_list_by_price(self):
        price_object = self.are_visible('css', LocatorsSort.INVENTORY_PRICE, LocatorsSort.INVENTORY_PRICE)
        return self.generation_list(price_object)

    def save_list_by_name(self):
        name_object = self.are_visible('css', LocatorsSort.INVENTORY_NAME, LocatorsSort.INVENTORY_NAME)
        return self.generation_list(name_object)

    def check_sort_by_name_lists_az(self):
        actual_list = self.save_list_by_name()
        expected_list = list(actual_list)
        self.equal(natsorted(expected_list), actual_list)

    def check_sort_by_name_lists_za(self):
        actual_list = self.save_list_by_name()
        expected_list = list(actual_list)
        self.equal(natsorted(expected_list, reverse=True), actual_list)

    def check_sort_by_price_lists_az(self):
        actual_list = self.save_list_by_price()
        expected_list = list(actual_list)
        self.equal(natsorted(expected_list), actual_list)

    def check_sort_by_price_lists_za(self):
        actual_list = self.save_list_by_price()
        expected_list = list(actual_list)
        self.equal(natsorted(expected_list, reverse=True), actual_list)
