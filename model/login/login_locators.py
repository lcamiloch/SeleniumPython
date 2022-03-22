"""In this module is stored the class with the login page locators"""
from selenium.webdriver.common.by import By


class LoginLocators:
    """The login page locators are stored in this class"""
    INPUT_USER_NAME = (By.XPATH, "//input[@id='username_input']")
    INPUT_PASSWORD = (By.XPATH, "//input[@id='password_input']")
    BUTTON_SIGN_IN = (By.XPATH, "//input[@id='login_submit']")
