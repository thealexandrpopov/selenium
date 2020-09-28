# selenium_framework
Custom framework for functional testing of web applications based on Selenium Webdriver, written in Python.

To build a test case follow these steps:

1. Duplicate the login_page file and input all required variables at the top.
2. Edit all functions that need to be run to achieve the expected result.
3. In the final two functions specify the assertions used to validate test results, positive and negative. 
4. Duplicate test_login page and edit the functions to run the tests on your page.
5. Run your tests from the command line using py.test capabilities. By default tests will run in Firefox, but you can choose Chrome or IE as well by 
specifying the desired browser as an option "--browser", e.g. "py.test --browser Chrome". 

Note: Make sure that environment variables on your machine are set up with appropriate drivers. 
You can also edit the "driver_maker.py" file to include paths to executables of your drivers.
