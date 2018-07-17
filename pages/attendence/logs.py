from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class Logs(BasePage):
    log = cl.customLogger(logging.DEBUG)
    # Locators
    _table_elements = "tbody [role='row']:nth-of-type(1) .sorting_1"  # By CSS

    locator = None
    locatorType = None

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verifyLogs(self, tablename, name):
        db = self.dbGetElement(tablename, name)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyDetails(self, tablename1, name1):
        db = self.dbGetElement(tablename1, name1)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyAbsentees(self, tablename2, name2):
        db = self.dbGetElement(tablename2, name2)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyMoreOptions(self, tablename3, name3):
        db = self.dbGetElement(tablename3, name3)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyAddBtn(self, tablename4, name4):
        db = self.dbGetElement(tablename4, name4)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifySearchBar(self, tablename5, name5):
        db = self.dbGetElement(tablename5, name5)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyTable(self, tablename6, name6):
        time.sleep(3)
        db = self.dbGetElement(tablename6, name6)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyDropDown(self, tablename7, name7, tablename8, name8):
        db = self.dbGetElement(tablename7, name7)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        self.elementClick(self.locator, self.locatorType)
        db1 = self.dbGetElement(tablename8, name8)
        try:
            self.locator = db1[0]
            self.locatorType = db1[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def LogsSmoke(self, tablename, name, tablename1, name1, tablename2, name2, tablename3, name3, tablename4, name4, tablename5, name5, tablename6, name6, tablename7, name7, tablename8, name8):
        self.nav.Attendence()
        self.waitForElement(self._table_elements, locatorType='css')
        result = self.verifyLogs(tablename, name)
        self.stat.mark(result, "Verify Logs")
        result1 = self.verifyAbsentees(tablename1, name1)
        self.stat.mark(result1, "Verify Absentees")
        result2 = self.verifyDetails(tablename2, name2)
        self.stat.mark(result2, "Verify Details")
        result3 = self.verifyMoreOptions(tablename3, name3)
        self.stat.mark(result3, "Verify More Options")
        result4 = self.verifyAddBtn(tablename4, name4)
        self.stat.mark(result4, "Verify Add Button")
        result5 = self.verifySearchBar(tablename5, name5)
        self.stat.mark(result5, "Verify Search Bar")
        result6 = self.verifyTable(tablename6, name6)
        self.stat.mark(result6, "Verify Table")
        result7 = self.verifyDropDown(tablename7, name7, tablename8, name8)
        self.stat.markFinal("Test_Logs", result7, "Verify Drop Down")

    def verifyTextLogs(self, logs1, logs):
        db = self.dbGetElement(logs1, logs)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")

        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(logs1, logs)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextName(self, logs2, name):
        db = self.dbGetElement(logs2, name)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("###Table name or Column name incorrect!!!")

        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(logs2, name)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextDateTime(self, logs3, datetime):
        db = self.dbGetElement(logs3, datetime)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("###Table name or Column name incorrect!!!")
        exceptedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(logs3, datetime)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, exceptedText)
        return result

    def verifyTextStatus(self, logs4, status):
        db = self.dbGetElement(logs4, status)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("###Table name or Column name incorrect!!!")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(logs4, status)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextAbsentees(self, logs5, absentees):
        db = self.dbGetElement(logs5, absentees)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("###Table name or Column name incorrect!!!")
        exceptedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(logs5, absentees)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, exceptedText)
        return result

    def verifyTextDetail(self, logs6, detail):
        db = self.dbGetElement(logs6, detail)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("###Table name or Column name incorrect!!!")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(logs6, detail)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def LogsText(self, logs1, logs, logs2, name, logs3, datetime, logs4, status, logs5, absentees, logs6, detail):
        result = self.verifyTextLogs(logs1, logs)
        self.stat.mark(result, "Verify Text Logs")
        result1 = self.verifyTextName(logs2, name)
        self.stat.mark(result1, "Verify Text Name")
        result2 = self.verifyTextDateTime(logs3, datetime)
        self.stat.mark(result2, "Verify Text Date Time")
        result3 = self.verifyTextStatus(logs4, status)
        self.stat.mark(result3, "Verify Text Status")
        result4 = self.verifyTextAbsentees(logs5, absentees)
        self.stat.mark(result4, "Verify Text Absentees")
        result5 = self.verifyTextDetail(logs6, detail)
        self.stat.markFinal("Test_ Log Text", result5, "Verify Text Detail")

