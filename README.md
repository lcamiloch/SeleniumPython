# Introduction
***
This automated script is responsible for testing the operation of the different notebooks of the jupyter notebooks.

The flows tested are:
* Login
* Global Settings notebook
* Direct Inversion notebbok


## Technologies
***
A list of technologies used within the project:
* [Python](https://www.python.org/): Version 3.7
* [Selenum](https://selenium-python.readthedocs.io/): Version 4.0 
* [Behave](https://behave.readthedocs.io/en/stable/): Version 1.2

## Installation
***
A little intro about the installation. 
```
$ git clone https://tfs.roseninspection.net/tfs/RNDCollection/Atlas/_git/DemoNotebook
$ cd ../e2e/demonotebook_e2e
$ pip install selenium
$ pip install behave
```
Download the HP Sure Click Secure Browser (BrChrome v92.0.4515.162) driver from the page:
* https://chromedriver.chromium.org/downloads (Download the same version of your browser)

and copy the driver to the path "C:\Automation\"

The user's credentials must be configured in the "properties.ini" file in the user and password variables

Side information: 
Suggestion to use the script with the pycharm IDE

## Execution
***
To execute the script, the following statement must be typed via console and enter:
```
behave --junit .\features\"{feature to be executed}"
```
example:
```
[Login flow] -> behave --junit .\features\login.feature
```
