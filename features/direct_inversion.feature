Feature: Direct Inversion execution

  Background: Login and global settings successful
    Given the customer wants to into to the demo notebook
    When he enters his credentials
    Then he should see the home page of demo notebook

    Given the customer is in the GlobalSettings notebook
    When he executes the cells of the notebook
    Then he should see all cells executed correctly


    Scenario: Successful execution of demo Notebook direct inversion
      Given the customer is in the DirectInversion notebook
      When he execute the cells of the direct inversion notebook
      Then he should see all the direct inversion notebook cells executed correctly