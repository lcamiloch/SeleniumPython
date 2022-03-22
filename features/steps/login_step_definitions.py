"""Step definition of the Login"""
from behave import given, when, then  # pylint: disable=no-name-in-module
from model.login.login_page import LoginPage
from model.home.home_page import HomePage


@given("the customer wants to into to the demo notebook")
def initial_step_login(context):
    """Executes the initial conditions of the test"""
    context.login = LoginPage(context.driver, context.wait)
    context.HomePage = HomePage(context.driver, context.wait)


@when("he enters his credentials")
def set_input_and_enter(context):
    """Enter the user's credentials"""
    context.login.set_user_name()
    context.login.set_password()
    context.login.click_on_sign_in()


@then("he should see the home page of demo notebook")
def check_home_page(context):
    """Validates that the user is on the home page"""
    assert context.HomePage.validation_home_page()
