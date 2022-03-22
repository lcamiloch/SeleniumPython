"""Step definition of the Global Settings notebook"""
from behave import given, when, then  # pylint: disable=no-name-in-module
from model.global_settings.global_settings_page import GlobalSettingsPage


@given("the customer is in the GlobalSettings notebook")
def initial_step_global_settings(context):
    """Executes the initial conditions of the test"""
    context.GlobalSettingsPage = GlobalSettingsPage(context.driver, context.wait)
    context.HomePage.open_global_settings_notebook()


@when("he executes the cells of the notebook")
def execution_all_cells_global_settings(context):
    """Execute the test actions"""
    context.GlobalSettingsPage.run_first_cell_global_settings()
    context.GlobalSettingsPage.run_second_cell_global_settings()
    context.GlobalSettingsPage.run_third_cell_global_settings()


@then("he should see all cells executed correctly")
def check_execution_global_settings(context):
    """Performs the test validations and closes the notebook tabs."""
    assert context.GlobalSettingsPage.validate_run_third_cell()
    context.HomePage.close_global_setting_notebook()
    context.HomePage.discard_changes()
    context.HomePage.unselect_global_settings()
