import scribe
import logging
from pages.carcass_page import CarcassPage
from toolbox import Toolbox


class LoginPage(CarcassPage):
    log = scribe.customLogger(logging.DEBUG)
    tool = Toolbox()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # All locator variables for the elements from the page go here:
    _login_link = "//div[@class='header__user']/a"
    _email_field = "office-auth-login-username"
    _password_field = "office-login-form-password"
    _login_button = "//button[contains(text(), 'Log in')]"
    _login_validated_message = "//div[@class='msrpc-promo']"
    _login_error_message = "//div[@class='jGrowl-notification alert ui-state-highlight ui-corner-all office-message-error']"

    # All test data goes here:
    valid_email = "alexandrpopovme@gmail.com"
    valid_password = "Miralova2020$"
    invalid_email = tool.getuniqueemail()
    invalid_password = tool.getuniquepassword()


    def clickLoginLink(self):
        self.elementClick(self._login_link)

    def enterEmail(self, email, typeOfLocator="id"):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password, typeOfLocator="id"):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button)

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        """
        Checks for a specific element that is present only if login is successful.
        """
        self.waitForElement(self._login_error_message)
        result = self.isElementPresent(self._login_validated_message)
        return result

    def verifyLoginFailed(self):
        """
        Checks if error message is present, returns True if it is.
        """
        result = self.isElementPresent(self._login_error_message)
        return result

    def verifyLoginTitle(self):
        """
        Calls verifyPageTitle function from the carcass page and checks if the current page is the expected one.
        """
        return self.verifyPageTitle("Sign In")
