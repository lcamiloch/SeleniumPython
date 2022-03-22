"""This module contains the class with the most common methods to interact with the pages"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class PageObject:
    """This class contains the common methods to interact with a page"""

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.actions = ActionChains(self.driver)

    def do_click(self, locator: By):
        """
        Click on a page element
        :param locator
        """
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def do_double_click(self, locator: By):
        """
        Double click on a page element
        :param locator
        """
        self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        self.actions.double_click(self.driver.find_element_by_xpath(locator)).perform()

    def do_send_keys(self, locator: By, text: str):
        """
        Sends keys to an input element on the page
        :param locator
        :param text
        """
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator: By) -> str:
        """
        Gets the text of a page element
        :param locator
        """
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def wait_element(self, locator: By):
        """
        Waits for a page element to become visible
        :param locator:
        """
        self.wait.until(EC.visibility_of_element_located(locator))

    def function_control_enter(self):
        """Execute the CTRL + ENTER key combination"""
        self.actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).perform()

    def element_is_displayed(self, locator: By) -> bool:
        """
        Checks that an element is visible and returns a boolean
        :param locator
        :return bool
        """
        self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        return self.driver.find_element_by_xpath(locator).is_displayed()
