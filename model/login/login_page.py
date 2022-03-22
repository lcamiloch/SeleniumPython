"""This module contains the methods of the login page"""
from model.utilities.config_manager import ConfigManager
from model.utilities.notebook_page_object import NotebookPageObject
from model.utilities.logging_config import Log
from model.login.login_locators import LoginLocators


class LoginPage(NotebookPageObject, LoginLocators):
    """This class contains the methods for using the login page"""

    def __init__(self, driver, wait):
        NotebookPageObject.__init__(self, driver, wait)
        self.log = Log().get_logger()

    def set_user_name(self):
        """Enter the user name"""
        self.do_send_keys(self.INPUT_USER_NAME, ConfigManager.get_value("user"))
        self.log.info("Enter user name successfully")

    def set_password(self):
        """Enter the password"""
        self.do_send_keys(self.INPUT_PASSWORD, ConfigManager.get_value("password"))
        self.log.info("Enter password successfully")

    def click_on_sign_in(self):
        """Click on the sign in button"""
        self.do_click(self.BUTTON_SIGN_IN)
        self.log.info("Click on the sign in button successfully")
