from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class Absentees(BasePage):
    log = cl.customLogger(logging.DEBUG)
    locator = None
    locatorType = None
    # Locators
    _side_menu = "//ul[@id='cd-primary-nav']/li[1]"  # By Xpath
    _attendance = "Attendance"  # By Link
    _logs = "Logs"  # By Link
    _details = "Detail"  # By Link
    _absentees = "Absentees"  # By Link
    _more_options = "[data-toggle='collapse']"  # By CSS
    _search_bar = "#basic_search [type]"  # By CSS
    _add_new = ".btn-blue.btn-action"  # By CSS
    _table = "tbody [role='row']:nth-of-type(1) .sorting_1"  # By CSS
    _department = ".dataTables_scrollHeadInner [role] [align='left']:nth-of-type(1)"  # By CSS
    _name = ".dataTables_scrollHeadInner [role] [align='left']:nth-of-type(2)"  # By CSS
    _phone1 = ".dataTables_scrollHeadInner [role] [align='left']:nth-of-type(3)"  # By CSS
    _phone2 = ".dataTables_scrollHeadInner [role] [align='left']:nth-of-type(4)"  # By CSS

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickAbsentees(self, AbsenteesT, absentees):
        db = self.dbGetElement(AbsenteesT, absentees)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        self.elementClick(self.locator, self.locatorType)

    def verifyLog(self, Absentees1, AbsenteesC):
        db = self.dbGetElement(Absentees1, AbsenteesC)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyDetails(self, Absentees2, detail):
        db = self.dbGetElement(Absentees2, detail)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyMoreOptions(self, Absentees3, moreoptions):
        db = self.dbGetElement(Absentees3, moreoptions)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifySearchBar(self, Absentees4, searchbar):
        db = self.dbGetElement(Absentees4, searchbar)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyAddBtn(self, Absentees5, addnew):
        db = self.dbGetElement(Absentees5, addnew)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyTable(self, Absentees7, table):
        db = self.dbGetElement(Absentees7, table)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def waitForTable(self, Absentees6, table):
        db = self.dbGetElement(Absentees6, table)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        self.waitForElement(self.locator, self.locatorType)

    def absenteesSmoke(self, AbsenteesT, absentees, Absentees1, logsC, Absentees2, detail, Absentees3, moreoptions, Absentees4, searchbar, Absentees5, addnew, Absentees6, table, Absentees7, table1):
        self.nav.Attendence()
        self.clickAbsentees(AbsenteesT, absentees)
        result = self.verifyLog(Absentees1, logsC)
        self.stat.mark(result, "Verify Logs")
        result1 = self.verifyDetails(Absentees2, detail)
        self.stat.mark(result1, "Verify Details")
        result2 = self.verifyMoreOptions(Absentees3, moreoptions)
        self.stat.mark(result2, "Verify More Options")
        result3 = self.verifySearchBar(Absentees4, searchbar)
        self.stat.mark(result3, "Verify Search Bar")
        result4 = self.verifyAddBtn(Absentees5, addnew)
        self.stat.mark(result4, "Verify Add Button")
        self.waitForTable(Absentees6, table)
        result5 = self.verifyTable(Absentees7, table1)
        self.stat.markFinal("Test_Absentees", result5, "Verify Table")

    def verifyTextAbsentees(self, absentees, absenteesC):
        db = self.dbGetElement(absentees, absenteesC)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(absentees, absenteesC)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextDetail(self, absentees1, detail):
        db = self.dbGetElement(absentees1, detail)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(absentees1, detail)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextLogs(self, absentees2, logs):
        db = self.dbGetElement(absentees2, logs)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(absentees2, logs)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextDepartment(self, absentees3, department):
        db = self.dbGetElement(absentees3, department)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(absentees3, department)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextName(self, absentees4, name):
        db = self.dbGetElement(absentees4, name)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(absentees4, name)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextPhone(self, absentees5, phone1):
        db = self.dbGetElement(absentees5, phone1)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(absentees5, phone1)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextPhone2(self, absentees6, phone2):
        db = self.dbGetElement(absentees6, phone2)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(absentees6, phone2)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def AbsenteesText(self, absentees, absenteesC, absentees1, detail, absentees2, logs, absentees3, department, absentees4, name, absentees5, phone1, absentees6, phone2):
        result = self.verifyTextAbsentees(absentees,absenteesC)
        self.stat.mark(result, "Verify Text Absentees")
        result1 = self.verifyTextDetail(absentees1, detail)
        self.stat.mark(result1, "Verify Text Detail")
        result2 = self.verifyTextLogs(absentees2, logs)
        self.stat.mark(result2, "Verify Text Logs")
        result3 = self.verifyTextDepartment(absentees3, department)
        self.stat.mark(result3, "Verify Text Department")
        result4 = self.verifyTextName(absentees4, name)
        self.stat.mark(result4, "Verify Text Name")
        result5 = self.verifyTextPhone(absentees5, phone1)
        self.stat.mark(result5, "Verify Text Phone1")
        result6 = self.verifyTextPhone2(absentees6, phone2)
        self.stat.markFinal("Test_Text Absentees ", result6, "Verify Text Phone2")