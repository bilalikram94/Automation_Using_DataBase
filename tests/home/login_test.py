import pytest
import unittest
from utilities.teststatus import Status
from pages.home.login_page import LoginPage
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData
"""
when using pytest the test cases must start with test_("testname") and the test must start with small 't' otherwise 
the test will not be collected 
"""


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class LoginTests(unittest.TestCase, LoginPage):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)

        """
        Need to verify two verification points
        1 fails, code will not go to the next verification point
        If assert fails, it stops current test execution and moves to the next test method.
        """

    @pytest.mark.run(order=1)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/loginPageXpath.csv"))
    @unpack
    def test_invalidLogin(self, xpath, selector, email, _email, password, _password, lgnBtn, path, path1, select):
        self.lp.logout(xpath, selector)
        self.lp.login(email, _email, password, _password, lgnBtn, path)
        result = self.lp.verifyLoginFailed1(path1, select)
        self.ts.markFinal("test_invalidLogin", result, "Login wasn't successful")

    @pytest.mark.run(order=2)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/validlogin.csv"))
    @unpack
    def test_validLogin(self, email, _email, password, _password, lgnBtn, path, path1, select):
        self.lp.login(email, _email, password, _password, lgnBtn, path)
        result = self.lp.verifyLogin(path1, select)
        self.ts.markFinal("test_validLogin", result, "Login was Successful")

   # @pytest.mark.run(order=3)
    #def test_validlogout(self):
    #    self.lp.logout()
    #    result = self.lp.verifyLogoutSuccess()
    #    self.ts.markFinal("test_validLogout", result, "Logout successful")
