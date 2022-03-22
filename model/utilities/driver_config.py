"""This module contains the class in charge of configuring the selenium driver"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from model.utilities.config_manager import ConfigManager
from model.utilities.logging_config import Log


class SetParameterDriver:
    """This class contains the methods that configure to use the driver"""

    @staticmethod
    def driver_configuration() -> webdriver:
        """
        Initial driver configuration
        :return webdriver
        """
        options = webdriver.ChromeOptions()
        if ConfigManager.get_value("headlessMode") == "Enabled":
            options.add_argument("--headless")
            options.add_experimental_option('excludeSwitches', ["enable-logging"])
        else:
            options.add_experimental_option("excludeSwitches", ["enable-logging"])

        if ConfigManager.get_value("useBrChrome") == "yes":
            options.binary_location = ConfigManager.get_value("pathBrowser")
            driver = webdriver.Chrome(options=options, executable_path=ConfigManager.get_value("pathDriverBrChrome"))
        else:
            driver = webdriver.Chrome(options=options, executable_path=ConfigManager.get_value("pathDriver"))

        driver.get(ConfigManager.get_value("baseURL"))
        driver.maximize_window()
        Log().get_logger().info("The driver is successfully configured")
        return driver

    @staticmethod
    def set_waiting_time(driver) -> webdriver:
        """
        Configuration of the driver waits
        :param driver
        :return WebdriverWait
        """
        Log().get_logger().info("Timeout successfully configured")
        return WebDriverWait(driver, ConfigManager.get_value("ExpectedWaitingTime"))

    @staticmethod
    def close_driver(driver):
        """
        Closes the driver after execution
        :param driver
        """
        driver.close()
        driver.quit()
        Log().get_logger().info("Driver successfully closed")
