"""This module contains the class with the most common methods for interacting with the demo notebook page"""
from selenium.webdriver.common.by import By
from model.utilities.base_page_object import PageObject


class NotebookPageObject(PageObject):
    """This class contains the common methods to interact with demo notebook page"""

    def __init__(self, driver, wait):
        PageObject.__init__(self, driver, wait)

    def select_and_execute_cell(self, locator_expected: By, locator: By):
        """
        selects a cell and runs it
        :param locator_expected
        :param locator
        """
        self.wait_element(locator_expected)
        self.do_click(locator)
        self.function_control_enter()
