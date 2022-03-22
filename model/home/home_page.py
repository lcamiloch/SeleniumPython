"""This module contains the methods of the home page"""
from model.home.home_locators import HomeLocators
from model.utilities.base_page_object import PageObject
from model.utilities.logging_config import Log


class HomePage(PageObject, HomeLocators):
    """this class contains the methods for using the home page"""

    def __init__(self, driver, wait):
        PageObject.__init__(self, driver, wait)
        self.log = Log().get_logger()

    def validation_home_page(self) -> bool:
        """
        validates login to the demo notebook home page
        :return bool
        """
        validation = self.get_text(self.TEXT_TITLE_COLUMN) == "Name"
        self.log.info("*** Home page validation successfully ***")
        return validation

    def close_global_setting_notebook(self):
        """closes the global settings notebook"""
        self.do_click(self.ICON_CLOSE_GLOBAL_SETTINGS)
        self.log.info("Closed the global settings notebook")

    def close_direct_inversion_notebook(self):
        """closes the direct inversion notebook"""
        self.do_click(self.ICON_CLOSE_DIRECT_INVERSION)
        self.log.info("Closed the direct inversion notebook")

    def discard_changes(self):
        """Click on the discard changes button"""
        self.do_click(self.BUTTON_DISCARD)
        self.log.info("Changes discarded in the notebook")

    def unselect_global_settings(self):
        """Deselect global notebook settings"""
        self.do_click(self.LINK_TEXT_GLOBAL_SETTINGS)
        self.log.info("The selection of the global settings notebook has been removed")

    def open_global_settings_notebook(self):
        """Open the global settings notebook"""
        self.do_double_click(self.locators["link_text_global_settings_xpath"])
        self.log.info("Open global settings notebook")

    def open_direct_inversion_notebook(self):
        """Open the direct inversion notebook"""
        self.actions.reset_actions()
        self.wait_element(self.LINK_TEXT_DIRECT_INVERSION)
        self.actions.double_click(
            self.driver.find_element_by_xpath(self.locators["link_text_direct_inversion_xpath"])).perform()
        self.log.info("Open direct inversion notebook")

    def log_out(self):
        self.do_click()
