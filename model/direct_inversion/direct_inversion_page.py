"""This module contains the methods of the direct inversion notebook"""
import time
from model.direct_inversion.direct_inversion_locators import DirectInversionLocators
from model.global_settings.global_settings_page import GlobalSettingsLocators as gsl
from model.utilities.notebook_page_object import NotebookPageObject
from model.utilities.logging_config import Log


class DirectInversionPage(NotebookPageObject, DirectInversionLocators):
    """This class contains the methods for using the direct inversion notebook"""

    def __init__(self, driver, wait):
        NotebookPageObject.__init__(self, driver, wait)
        self.log = Log().get_logger()

    def run_first_cell_direct_inversion(self):
        """Execution of the first cell of the direct inversion notebook"""
        time.sleep(1)
        self.do_click(self.FIRST_CELL)
        time.sleep(1)
        self.function_control_enter()
        self.log.info("First cell of the direct inversion notebook executed")

    def run_second_cell_direct_inversion(self):
        """Execution of the second cell of the direct inversion notebook"""
        self.select_and_execute_cell(
            gsl.TEXT_VALIDATION_FIRST_CELL, self.SECOND_CELL)
        self.log.info("Second cell of the direct inversion notebook executed")

    def run_third_cell_direct_inversion(self):
        """Execution of the third cell of the direct inversion notebook"""
        self.select_and_execute_cell(
            self.TEXT_VALIDATION_SECOND_CELL, self.THIRD_CELL)
        self.log.info("Third cell of the direct inversion notebook executed")

    def run_fourth_cell_direct_inversion(self):
        """Execution of the fourth cell of the direct inversion notebook"""
        self.select_and_execute_cell(
            gsl.TEXT_VALIDATION_FIFTH_CELL, self.FOURTH_CELL)
        self.log.info("Fourth cell of the direct inversion notebook executed")

    def run_fifth_cell_direct_inversion(self):
        """Execution of the fifth cell of the direct inversion notebook"""
        self.select_and_execute_cell(
            self.TEXT_VALIDATION_FOURTH_CELL, self.FIFTH_CELL)
        self.log.info("Fifth cell of the direct inversion notebook executed")

    def run_sixth_cell_direct_inversion(self):
        """Execution of the sixth cell of the direct inversion notebook"""
        self.select_and_execute_cell(
            self.TEXT_VALIDATION_FIFTH_CELL, self.SIXTH_CELL)
        self.log.info("Sixth cell of the direct inversion notebook executed")

    def run_seventh_cell_direct_inversion(self):
        """Execution of the seventh cell of the direct inversion notebook"""
        self.select_and_execute_cell(
            self.TEXT_VALIDATION_SIXTH_CELL, self.SEVENTH_CELL)
        self.log.info("Seventh cell of the direct inversion notebook executed")

    def run_eighth_cell_direct_inversion(self):
        """Execution of the eighth cell of the direct inversion notebook"""
        self.select_and_execute_cell(
            self.TEXT_VALIDATION_SEVENTH_CELL, self.EIGHTH_CELL)
        self.log.info("Eighth cell of the direct inversion notebook executed")

    def run_ninth_cell_direct_inversion(self):
        """Execution of the ninth cell of the direct inversion notebook"""
        self.select_and_execute_cell(
            self.TEXT_VALIDATION_EIGHTH_CELL, self.NINTH_CELL)
        self.log.info("Ninth cell of the direct inversion notebook executed")

    def run_tenth_cell_direct_inversion(self):
        """Execution of the tenth cell of the direct inversion notebook"""
        self.select_and_execute_cell(
            self.TEXT_VALIDATION_NINTH_CELL, self.TENTH_CELL)
        self.log.info("Tenth cell of the direct inversion notebook executed")

    def validate_direct_inversion_run(self) -> bool:
        """
        Check the answer of the last cell
        :return bool
        """
        validation = self.element_is_displayed(self.locators["text_validation_tenth_cell_xpath"])
        self.log.info("*** Last cell of the direct inversion notebook executed ***")
        return validation
