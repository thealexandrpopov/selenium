from pages.login_page import LoginPage
from judge import AssertStatus
import pytest
from toolbox import Toolbox
import unittest


@pytest.mark.usefixtures("setUp", "oneTimeSetUp")
class LoginTests(unittest.TestCase):

    valid_email = "alexandrpopovme@gmail.com"
    valid_password = "Miralova2020$"

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.assertStatus = AssertStatus(self.driver)
        self.tool = Toolbox()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        email = self.tool.getuniqueemail()
        password = self.tool.getuniquepassword()

        self.lp.login(email, password)
        result = self.lp.verifyLoginFailed()
        assert result == True

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        login = self.valid_email
        password = self.valid_password
        self.lp.login(login, password)
        result1 = self.lp.verifyLoginTitle()
        self.assertStatus.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.assertStatus.markFinal("test_validLogin", result2, "Login Verification")
