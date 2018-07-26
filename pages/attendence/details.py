from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class Details(BasePage):
    log = cl.customLogger(logging.DEBUG)
    locator = None
    locatorType = None

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verifyLogs(self, detail, logs):
        db = self.DBGetElement(detail, logs)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyAbsentees(self, detail1, absentees):
        db = self.DBGetElement(detail1, absentees)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")

        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifySearchBar(self, detail2, searchbar):
        db = self.DBGetElement(detail2, searchbar)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyMoreOptions(self, detail3, moreoptions):
        db = self.DBGetElement(detail3, moreoptions)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyAddNew(self, detail4, addnew):
        db = self.DBGetElement(detail4, addnew)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")

        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyExport(self, detail5, export):
        db = self.DBGetElement(detail5, export)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def waitForTable(self, detail6, table,):
        db = self.DBGetElement(detail6, table)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        self.waitForElement(self.locator, self.locatorType)

    def verifyTable(self, detail7, table1):
        db = self.DBGetElement(detail7, table1)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def DetailsSmoke(self, detail, logs, detail1, absentees, detail2, searchbar, detail3, moreoptions, detail4, export, detail5, addnew, detail6, table, detail7, table1):
        self.nav.Details()
        result = self.verifyLogs(detail, logs)
        self.stat.mark(result, "Verify Details")
        result1 = self.verifyAbsentees(detail1, absentees)
        self.stat.mark(result1, "Verify Absentees")
        result2 = self.verifySearchBar(detail2, searchbar)
        self.stat.mark(result2, "Verify Search Bar")
        result3 = self.verifyMoreOptions(detail3, moreoptions)
        self.stat.mark(result3, "Verify More Options")
        result4 = self.verifyExport(detail4, export)
        self.stat.mark(result4, "Verify Export")
        result5 = self.verifyAddNew(detail5, addnew)
        self.stat.mark(result5, "Verify Add New")
        self.waitForTable(detail6, table)
        result6 = self.verifyTable(detail7, table1)
        self.stat.markFinal("Test_Details Smoke", result6, "Verify Table")

    def verifyTextDay(self, detail, day):
        db = self.DBGetElement(detail, day)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(detail, day)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextDate(self, detail1, date):
        db = self.DBGetElement(detail1, date)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(detail1, date)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextTimeIn(self, detail2, timein):
        db = self.DBGetElement(detail2, timein)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(detail2, timein)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextTimeOut(self, detail3, timeout):
        db = self.DBGetElement(detail3, timeout)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(detail3, timeout)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTimeSpent(self, detail4, timespent):
        db = self.DBGetElement(detail4, timespent)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(detail4, timespent)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextBreakTime(self, detail5, breaktime):
        db = self.DBGetElement(detail5, breaktime)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(detail5, breaktime)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextWorktime(self, detail6, worktime):
        db = self.DBGetElement(detail6, worktime)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(detail6, worktime)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextAbsentees(self, detail7, absentees):
        db = self.DBGetElement(detail7, absentees)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(detail7, absentees)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextDetail(self, detail8, detailC):
        db = self.DBGetElement(detail8, detailC)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(detail8, detailC)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextLogs(self, detail9, logs):
        db = self.DBGetElement(detail9, logs)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(detail9, logs)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextAddNew(self, detail10, addnew):
        db = self.DBGetElement(detail10, addnew)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(detail10, addnew)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextExport(self, detail11, export):
        db = self.DBGetElement(detail11, export)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(detail11, export)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def DetailsVerifyText(self, detail, day, detail1, date, detail2, timein, detail3, timeout, detail4, timespent,
                          detail5, breaktime, detail6, worktime, detail7, absentees, detail8, detailC, detail9, logs,
                          detail10, addnew, detail11, export):
        self.nav.Details()
        result = self.verifyTextDay(detail, day)
        self.stat.mark(result, "Verify Text Day ")
        result1 = self.verifyTextDate(detail1, date)
        self.stat.mark(result1, "Verify Text Date")
        result2 = self.verifyTextTimeIn(detail2, timein)
        self.stat.mark(result2, "Verify Text Time In")
        result3 = self.verifyTextTimeOut(detail3, timeout)
        self.stat.mark(result3, "Verify Text Time Out")
        result4 = self.verifyTimeSpent(detail4, timespent)
        self.stat.mark(result4, "Veirfy Text Time Spent")
        result5 = self.verifyTextBreakTime(detail5, breaktime)
        self.stat.mark(result5, "Verify Text Break Time")
        result6 = self.verifyTextWorktime(detail6, worktime)
        self.stat.mark(result6, "Verify Text Work Time")
        result7 = self.verifyTextAbsentees(detail7, absentees)
        self.stat.mark(result7, "Verify Text Absentees")
        result8 = self.verifyTextDetail(detail8, detailC)
        self.stat.mark(result8, "Verify Text Detail")
        result9 = self.verifyTextLogs(detail9, logs)
        self.stat.mark(result9, "Verify Text Logs")
        result10 = self.verifyTextAddNew(detail10, addnew)
        self.stat.mark(result10, "Verify Text Add New")
        result11 = self.verifyTextExport(detail11, export)
        self.stat.markFinal("Test_Text_Detail", result11, "Verify Text Export")
