from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    # Locators
    _login_link = "Login"  # By Link-Text
    _email_field = "el1"  # By ID
    _password_field = "el4"  # By ID
    _login_button = "//input[@type='submit']"  # By Xpath
    _login_success = ".logo-cubix"  # By CSS Selector
    _failed_login = ".alert-dismissible"  # By CSS Selector
    _user_image = ".user-image"  # By CSS Selector
    _logout_button = "Logout"  # By LinkText
    _logout_success_text = ".alert-dismissible"  # By CSS Selector
    _forget_password = "Forget Password?"  # By Link Text

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enterEmail(self, email, _email):
        self.sendKeys(email, _email)

    def enterPassword(self, password, _password):
        self.sendKeys(password, _password)

    def clickLoginBtn(self, lgnBtn, path):
        self.elementClick(lgnBtn, path)

    def verifyLogin(self, path1, select):
        result = self.isElementPresent(path1, select)
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._failed_login, locatorType='css')
        return result

    def verifyLoginFailed1(self, path1, select):
        result = self.isElementPresent(path1, select)
        return result

    def userImage(self, xpath, selector):
        self.elementClick(xpath, selector)
        self.util.sleep(2)

    def logoutButton(self):
        self.elementClick(self._logout_button, locatorType='link')
        self.util.sleep(2)

    def verifyLogoutSuccess(self):
        time.sleep(2)
        text = self.getText(self._forget_password, locatorType='link')
        result = self.util.verifyTextContains("Forget Password?", text)
        return result

    def login(self, _email, email, _password, password, lgnBtn, path):
        self.enterEmail(_email, email)
        self.enterPassword(_password, password)
        self.clickLoginBtn(lgnBtn, path)

    def logout(self, xpath, selector):
        self.userImage(xpath, selector)
        self.logoutButton()

    def conflogin(self):
        self.sendKeys("networks@cubixlabs.com", self._email_field)
        self.sendKeys("Cubix@786", self._password_field)
        self.elementClick(self._login_button, locatorType='xpath')
