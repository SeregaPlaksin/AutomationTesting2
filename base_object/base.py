from typing import List

from base_object.locators import Locators
from utilities.logger import *
import logging as log

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from base_object.errors import AssertionErrors
from selenium.webdriver.remote.webelement import WebElement


class BaseObject:
    log = log_method(logLevel=log.INFO)
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def __selenium_by(self, find_by=None):
        selectors_dict = {'css': By.CSS_SELECTOR,
                          'xpath': By.XPATH,
                          'id': By.ID,
                          'name': By.NAME,
                          'class': By.CLASS_NAME,
                          'partial_link_text': By.PARTIAL_LINK_TEXT,
                          'link_text': By.LINK_TEXT,
                          'tag_name': By.TAG_NAME}
        return selectors_dict[find_by]

    def is_visible(self, find_by, locator):
        self.log.info(f'element is_present - "{locator}"')
        return self.wait.until(ec.visibility_of_element_located((self.__selenium_by(find_by), locator)))

    def is_present(self, find_by, locator):
        self.log.info(f'element is_present -"{locator}"')
        return self.wait.until(ec.presence_of_element_located((self.__selenium_by(find_by), locator)))

    def is_clickable(self, find_by, locator):
        self.log.info(f'element is_clickable - "{locator}"')
        return self.wait.until(ec.element_to_be_clickable((self.__selenium_by(find_by), locator)))

    def are_visible(self, find_by, locator, locator_name) -> List[WebElement]:
        self.log.info(f'all element visible - "{locator}"')
        return self.wait.until(ec.visibility_of_all_elements_located((self.__selenium_by(find_by), locator)),
                               locator_name)

    def to_input(self, find_by, locator, text):
        self.log.info(f'input on - "{locator}"')
        self.is_visible(find_by, locator).send_keys(text)

    def to_text(self, find_by, locator):
        self.log.info(f'input text in - "{locator}"')
        return self.is_visible(find_by, locator).text

    def to_get_attribute(self, find_by, locator, name_attr):
        return self.is_visible(find_by, locator).get_attribute(name_attr)

    def to_click(self, find_by, locator):
        self.log.info(f'clicked on - "{locator}"')
        self.is_clickable(find_by, locator).click()

    def select_dropdown(self, find_by, locator, text):
        self.log.info(f'select dropdown - "{locator}"')
        dropdown = Select(self.is_visible(find_by, locator))
        return dropdown.select_by_visible_text(text)











