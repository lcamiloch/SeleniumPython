"""Step definition of the Direct Inversion notebook"""
from behave import given, when, then  # pylint: disable=no-name-in-module
from model.direct_inversion.direct_inversion_page import DirectInversionPage


@given("the customer is in the DirectInversion notebook")
def initial_step_direct_inversion(context):
    """Executes the initial conditions of the test"""
    context.DirectInversionPage = DirectInversionPage(context.driver, context.wait)
    context.HomePage.open_direct_inversion_notebook()


@when("he execute the cells of the direct inversion notebook")
def execution_all_cells_direct_inversion(context):
    """Execute the test actions"""
    context.DirectInversionPage.run_first_cell_direct_inversion()
    context.DirectInversionPage.run_second_cell_direct_inversion()
    context.DirectInversionPage.run_third_cell_direct_inversion()
    context.DirectInversionPage.run_fourth_cell_direct_inversion()
    context.DirectInversionPage.run_fifth_cell_direct_inversion()
    context.DirectInversionPage.run_sixth_cell_direct_inversion()
    context.DirectInversionPage.run_seventh_cell_direct_inversion()
    context.DirectInversionPage.run_eighth_cell_direct_inversion()
    context.DirectInversionPage.run_ninth_cell_direct_inversion()
    context.DirectInversionPage.run_tenth_cell_direct_inversion()


@then("he should see all the direct inversion notebook cells executed correctly")
def check_execution_direct_inversion(context):
    """Performs the test validations and closes the notebook tabs"""
    assert context.DirectInversionPage.validate_direct_inversion_run()
    context.HomePage.close_direct_inversion_notebook()
    context.HomePage.discard_changes()
