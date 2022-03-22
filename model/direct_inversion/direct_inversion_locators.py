"""In this module is stored the class with the direct inversion notebook locators"""
from selenium.webdriver.common.by import By


class DirectInversionLocators:
    """The direct inversion notebook locators are stored in this class"""
    locators = {
        "text_validation_tenth_cell_xpath": "//div[@class='jupyter-matplotlib-figure']/div[text()='Figure 2']"
    }

    FIRST_CELL = (By.XPATH, "//*[contains(text(),'DI-load-dependencies')]")
    SECOND_CELL = (By.XPATH, "//span[contains(text(),'DI-print-tech-specs')]")
    TEXT_VALIDATION_SECOND_CELL = (By.XPATH, "//a[contains(@href,'api/v0/tech-specs')]")
    THIRD_CELL = (By.XPATH, "//span[contains(text(),'DI-get-in-settings')]")
    FOURTH_CELL = (By.XPATH, "//span[contains(text(),'DI-print-dist-range')]")
    TEXT_VALIDATION_FOURTH_CELL = (By.XPATH, "(//pre[contains(text(),'start') and contains(text(),'end')])[2]")
    FIFTH_CELL = (By.XPATH, "//span[contains(text(),'DI-run-inversion')]")
    TEXT_VALIDATION_FIFTH_CELL = (By.XPATH, "//div[contains(text(),'100.0%, Success')]")
    SIXTH_CELL = (By.XPATH, "(//span[contains(text(),'DI-display-table')])[1]")
    TEXT_VALIDATION_SIXTH_CELL = (By.XPATH, "//th[contains(text(),'distance_m')]")
    SEVENTH_CELL = (By.XPATH, "//span[contains(text(),'DI-save-sb-results')]")
    TEXT_VALIDATION_SEVENTH_CELL = (By.XPATH, "//pre[contains(text(),'scratch')]")
    EIGHTH_CELL = (By.XPATH, "//span[contains(text(),'DI-print-channels')]")
    TEXT_VALIDATION_EIGHTH_CELL = (By.XPATH, "//pre[contains(text(),'HORIZONTAL')]")
    NINTH_CELL = (By.XPATH, "//span[contains(text(),'DI-get-image')]")
    TEXT_VALIDATION_NINTH_CELL = (By.XPATH, "//div[@class='jupyter-matplotlib-figure']/div[text()='Figure 1']")
    TENTH_CELL = (By.XPATH, "//span[contains(text(),'DI-get-image-w-boxes')]")
