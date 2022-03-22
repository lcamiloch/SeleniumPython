Feature: Global settings execution

  Background: Login successful
    Given the customer wants to into to the demo notebook
    When he enters his credentials
    Then he should see the home page of demo notebook


    Scenario: Successful execution of demo Notebook global settings
      Given the customer is in the GlobalSettings notebook
      When he executes the cells of the notebook
      Then he should see all cells executed correctly