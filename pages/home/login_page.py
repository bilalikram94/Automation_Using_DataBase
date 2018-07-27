from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    locator = None
    locatorType = None

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

    def enterEmail(self, email, login, _email):
        db = self.DBGetElement(login, _email)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table Name or Column Name is Incorrect !!!")
        self.sendKeys(email, self.locator, self.locatorType)

    def enterPassword(self, password, login2, _password):
        db = self.DBGetElement(login2, _password)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table Name or Column Name is Incorrect")
        self.sendKeys(password, self.locator, self.locatorType)

    def clickLoginBtn(self, login3, loginBtn):
        db = self.DBGetElement(login3, loginBtn)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column Name is Incorrect !!!")
        self.elementClick(self.locator, self.locatorType)

    def verifyLogin(self, login4, vlogin):
        db = self.DBGetElement(login4, vlogin)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column name Incorrect !!!")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyLoginFailed(self, login5, flogin):
        db = self.DBGetElement(login5, flogin)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or column name Incorrect !!!")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyLoginFailed1(self, login6, logo):
        db = self.DBGetElement(login6, logo)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or column name Incorrect !!!")
        print(db)
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def userImage(self, login7, image):
        db = self.DBGetElement(login7, image)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or column name Incorrect !!!")
        self.elementClick(self.locator, self.locatorType)
        self.util.sleep(2)

    def logoutButton(self, login8, logout):
        db = self.DBGetElement(login8, logout)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or column name Incorrect !!!")
        self.elementClick(self.locator, self.locatorType)
        self.util.sleep(2)

    def verifyLogoutSuccess(self, login9, forgot):
        time.sleep(2)
        db = self.DBGetElement(login9, forgot)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column Name is Incorrect !!!")
        exceptedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(login9, forgot)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, exceptedText)
        return result

    def invalidLogin(self, email, login, _email, password, login2, _password, login3, loginBtn, login6, logo):
        time.sleep(3)
        self.enterEmail(email, login, _email)
        self.enterPassword(password, login2, _password)
        self.clickLoginBtn(login3, loginBtn)
        result = self.verifyLoginFailed1(login6, logo)
        self.stat.markFinal("Test_invalid Login", result, "Invalid Login")

    def validLogin(self, email, login, _email, password, login2, _password, login3, loginBtn, login4, vlogin):
        self.enterEmail(email, login, _email)
        self.enterPassword(password, login2, _password)
        self.clickLoginBtn(login3, loginBtn)
        result = self.verifyLogin(login4, vlogin)
        self.stat.markFinal("Test_valid Login", result, "Valid Login")

    def logout(self, login7, image, login8, logout):
        self.userImage(login7, image)
        self.logoutButton(login8, logout)

    def conflogin(self):
        self.sendKeys("networks@cubixlabs.com", self._email_field)
        self.sendKeys("Cubix@786", self._password_field)
        self.elementClick(self._login_button, locatorType='xpath')
