from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class SideMenu(BasePage):
    log = cl.customLogger(logging.DEBUG)
    locator = None
    locatorType = None

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickSideMenu(self, side, sidemenu):
        db = self.DBGetElement(side, sidemenu)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        self.elementClick(self.locator, self.locatorType)
        self.util.sleep(3)

    def verifyAttendance(self, side1, attendance):
        db = self.DBGetElement(side1, attendance)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyEmployee(self, side2, emp):
        db = self.DBGetElement(side2, emp)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifySupportTicket(self, side3, support):
        db = self.DBGetElement(side3, support)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyTraining(self, side4, train):
        db = self.DBGetElement(side4, train)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyTimeOff(self, side5, timeoff):
        db = self.DBGetElement(side5, timeoff)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def SideMenuSmoke(self, side, sidemenu, side1, attendance, side2, emp, side3, support, side4, train, side5, timeoff):
        self.clickSideMenu(side, sidemenu)
        result = self.verifyAttendance(side1, attendance)
        self.stat.mark(result, "Verify Attendence")
        result1 = self.verifyEmployee(side2, emp)
        self.stat.mark(result1, "Verify Employee")
        result2 = self.verifySupportTicket(side3, support)
        self.stat.mark(result2, "Verify Support Ticket")
        result3 = self.verifyTraining(side4, train)
        self.stat.mark(result3, "Verify Training")
        result4 = self.verifyTimeOff(side5, timeoff)
        self.stat.markFinal("Test_Side Menu", result4, "Verify Time Off")

    def verifyTextAttendance(self, side, attendance):
        db = self.DBGetElement(side, attendance)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(side, attendance)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextEmployees(self, side1, emp):
        db = self.DBGetElement(side1, emp)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(side1, emp)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextSupportTicket(self, side2, support):
        db = self.DBGetElement(side2, support)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(side2, support)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextTraining(self, side3, train):
        db = self.DBGetElement(side3, train)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(side3, train)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextTimeOff(self, side4, timeoff):
        db = self.DBGetElement(side4, timeoff)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(side4, timeoff)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def SideMenuText(self,  side, attendance, side1, emp, side2, support, side3, train, side4, timeoff):
        result = self.verifyTextAttendance(side, attendance)
        self.stat.mark(result, "Verify Text Attendence")
        result1 = self.verifyTextEmployees(side1, emp)
        self.stat.mark(result1, "Verify Text Employee")
        result2 = self.verifyTextSupportTicket(side2, support)
        self.stat.mark(result2, "Verify Text Support Ticket")
        result3 = self.verifyTextTraining(side3, train)
        self.stat.mark(result3, "Verify Text Training")
        result4 = self.verifyTextTimeOff(side4, timeoff)
        self.stat.markFinal("Test_Logs Text", result4, "Verify Text Time Off")