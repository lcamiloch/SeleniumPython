"""In this module is stored the class with the home page locators"""
from selenium.webdriver.common.by import By


class HomeLocators:
    """The home page locators are stored in this class"""
    locators = {
        "link_text_global_settings_xpath": "//span[@class='jp-DirListing-itemText']"
                                           "/span[text()='GlobalSettings.ipynb']//..",
        "link_text_direct_inversion_xpath": "//span[@class='jp-DirListing-itemText']"
                                            "/span[text()='DirectInversion.ipynb']//.."
    }

    TEXT_TITLE_COLUMN = (By.XPATH, "(//span[@class='jp-DirListing-headerItemText'])[1]")
    LINK_TEXT_GLOBAL_SETTINGS = (By.XPATH, "//span[@class='jp-DirListing-itemText']"
                                           "/span[text()='GlobalSettings.ipynb']//..")
    LINK_TEXT_DIRECT_INVERSION = (By.XPATH, "//span[@class='jp-DirListing-itemText']"
                                            "/span[text()='DirectInversion.ipynb']//..")
    ICON_CLOSE_GLOBAL_SETTINGS = (By.XPATH, "(//div[text()='GlobalSettings.ipynb'])[2]//following::div[1]")
    ICON_CLOSE_DIRECT_INVERSION = (By.XPATH, "(//div[text()='DirectInversion.ipynb'])[2]//following::div[1]")
    BUTTON_DISCARD = (By.XPATH, "//div[@class='jp-Dialog-buttonLabel'][text()='Discard']")
    TEXT_FILE = (By.XPATH, "//div[text()='File']")
    TEXT_LOG_OUT = (By.XPATH, "(//div[starts-with(@class,'lm-Menu-itemLabel')][text()='Log Out'])[1]")
