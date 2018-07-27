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

    @pytest.mark.run(order=2)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/loginPageXpath.csv"))
    @unpack
    def test_Login(self, email, login, _email, password, login2, _password,
                          login3, loginBtn, login6, logo):
        self.lp.invalidLogin(email, login, _email, password, login2, _password, login3, loginBtn, login6, logo)

    # @pytest.mark.run(order=2)
    # @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/validlogin.csv"))
    # @unpack
    # def test_validLogin(self, email, login, _email, password, login2, _password, login3, loginBtn, login4, vlogin):
    #     self.lp.validLogin(email, login, _email, password, login2, _password, login3, loginBtn, login4, vlogin)

    @pytest.mark.run(order=1)
    @data(*getCVSData("/home/bilalikram/PycharmProjects/Automation_Using_Database/logout.csv"))
    @unpack
    def test_LoginLogout(self, login7, image, login8, logout, login9, forgot):
        self.lp.logout(login7, image, login8, logout)
        result = self.lp.verifyLogoutSuccess(login9, forgot)
        self.ts.mark(result, "Logout successful")
