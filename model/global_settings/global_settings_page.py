"""This module contains the methods of the global settings notebook"""
import time
from model.global_settings.global_settings_locators import GlobalSettingsLocators
from model.utilities.notebook_page_object import NotebookPageObject
from model.utilities.logging_config import Log


class GlobalSettingsPage(NotebookPageObject, GlobalSettingsLocators):
    """this class contains the methods for using the global settings notebook"""

    def __init__(self, driver, wait):
        NotebookPageObject.__init__(self, driver, wait)
        self.log = Log().get_logger()

    def run_first_cell_global_settings(self):
        """Execution of the first cell of the global settings notebook"""
        time.sleep(1)
        self.do_click(self.FIRST_CELL)
        time.sleep(1)
        self.function_control_enter()
        self.log.info("First cell of the global settings notebook executed")

    def run_second_cell_global_settings(self):
        """Execution of the second cell of the global settings notebook"""
        self.select_and_execute_cell(
            self.TEXT_VALIDATION_FIRST_CELL, self.SECOND_CELL)
        self.log.info("Second cell of the global settings notebook executed")

    def run_third_cell_global_settings(self):
        """Execution of the third cell of the global settings notebook"""
        self.select_and_execute_cell(
            self.TEXT_VALIDATION_SECOND_CELL, self.THIRD_CELL)
        self.log.info("Third cell of the global settings notebook executed")

    def run_fourth_cell_global_settings(self):
        """Execution of the fourth cell of the global settings notebook"""
        self.select_and_execute_cell(
            self.TEXT_VALIDATION_THIRD_CELL, self.FOURTH_CELL)
        self.log.info("Fourth cell of the global settings notebook executed")

    def run_fifth_cell_global_settings(self):
        """Execution of the fifth cell of the global settings notebook"""
        time.sleep(2)
        self.select_and_execute_cell(
            self.TEXT_VALIDATION_FOURTH_CELL, self.FIFTH_CELL)
        self.log.info("Fifth cell of the global settings notebook executed")

    def run_sixth_cell_global_settings(self):
        """Execution of the sixth cell of the global settings notebook"""
        self.select_and_execute_cell(
            self.TEXT_VALIDATION_FIFTH_CELL, self.SIXTH_CELL)
        self.log.info("Sixth cell of the global settings notebook executed")

    def run_seventh_cell_global_settings(self):
        """Execution of the seventh cell of the global settings notebook"""
        self.select_and_execute_cell(
            self.TEXT_VALIDATION_SIXTH_CELL, self.SEVENTH_CELL)
        self.log.info("Seventh cell of the global settings notebook executed")

    def run_eighth_cell_global_settings(self):
        """Execution of the eighth cell of the global settings notebook"""
        self.select_and_execute_cell(
            self.TEXT_VALIDATION_SEVENTH_CELL, self.EIGHTH_CELL)
        self.log.info("Eighth cell of the global settings notebook executed")

    def run_ninth_cell_global_settings(self):
        """Execution of the ninth cell of the global settings notebook"""
        self.select_and_execute_cell(
            self.TEXT_VALIDATION_EIGHTH_CELL, self.NINTH_CELL)
        self.log.info("Ninth cell of the global settings notebook executed")

    def validate_global_settings_run(self) -> bool:
        """
        Check the answer of the last cell
        :return bool
        """
        validation = self.element_is_displayed(self.locators["text_validation_ninth_cell_xpath"])
        self.log.info("*** Last cell of the global settings notebook executed ***")
        return validation

    def validate_run_third_cell(self) -> bool:
        """
        Check the successful response of the third cell
        :return bool
        """
        validation = self.element_is_displayed(self.locators["text_validation_third_cell_xpath"])
        self.log.info("*** Cells required for the configuration were successfully executed ***")
        return validation
