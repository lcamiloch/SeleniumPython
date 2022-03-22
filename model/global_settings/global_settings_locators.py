"""In this module is stored the class with the global settings notebook locators"""
from selenium.webdriver.common.by import By


class GlobalSettingsLocators:
    """The global settings notebook locators are stored in this class"""
    locators = {
        "text_validation_ninth_cell_xpath": "//pre[contains(text(),'now be overwritten')]",
        "text_validation_third_cell_xpath": "//pre[contains(text(),'previously stored')]"
    }

    FIRST_CELL = (By.XPATH, "//span[contains(text(),'GS-load-dependencies')]")
    TEXT_VALIDATION_FIRST_CELL = (By.XPATH, "//b[text()='Reminder:']")
    SECOND_CELL = (By.XPATH, "//span[contains(text(),'GS-list-available-projects')]")
    TEXT_VALIDATION_SECOND_CELL = (By.XPATH, "//pre[text()='To download a run, please visit ']")
    THIRD_CELL = (By.XPATH, "//span[contains(text(),'GS-set-global-settings')]")
    TEXT_VALIDATION_THIRD_CELL = (By.XPATH, "//pre[contains(text(),'previously stored')]")
    FOURTH_CELL = (By.XPATH, "(//div[@class='CodeMirror-lines'][@role='presentation'])[8]")
    TEXT_VALIDATION_FOURTH_CELL = (By.XPATH, "//p[contains(text(),'create some globally')]")
    FIFTH_CELL = (By.XPATH, "(//div[@class='CodeMirror-lines'][@role='presentation'])[10]")
    TEXT_VALIDATION_FIFTH_CELL = (By.XPATH, "//pre[contains(text(),'Inspection Settings')]")
    SIXTH_CELL = (By.XPATH, "(//div[@class='CodeMirror-lines'][@role='presentation'])[12]")
    TEXT_VALIDATION_SIXTH_CELL = (By.XPATH, "(//pre[contains(text(),'Inspection Settings')])[2]")
    SEVENTH_CELL = (By.XPATH, "(//div[@class='CodeMirror-lines'][@role='presentation'])[14]")
    TEXT_VALIDATION_SEVENTH_CELL = (By.XPATH, "(//pre[contains(text(),'Inspection Settings')])[3]")
    EIGHTH_CELL = (By.XPATH, "(//div[@class='CodeMirror-lines'][@role='presentation'])[16]")
    TEXT_VALIDATION_EIGHTH_CELL = (By.XPATH, "(//pre[contains(text(),'previously stored')])[3]")
    NINTH_CELL = (By.XPATH, "(//div[@class='CodeMirror-lines'][@role='presentation'])[18]")
