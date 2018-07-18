from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class Details(BasePage):
    log = cl.customLogger(logging.DEBUG)
    locator = None
    locatorType = None
    # Locators
    _side_menu = "//ul[@id='cd-primary-nav']/li[1]"  # By Xpath
    _attendence = "Attendance"  # By Link
    _logs = "Logs"  # By Link
    _details = "Detail"  # By Link
    _absentees = "Absentees"  # By Link
    _more_options = "[data-toggle='collapse']"  # By CSS
    _search_bar = "#basic_search [type]"  # By CSS
    _add_new = ".btn-blue.btn-action"  # By CSS
    _export = "[name='export']"  # By CSS
    _table = "tbody tr:nth-of-type(1) .text-left"  # By CSS
    _day = "thead tr .text-center:nth-of-type(1)"  # By CSS
    _date = "thead tr .text-center:nth-of-type(2)"  # By CSS
    _time_in = "thead tr .text-center:nth-of-type(3)"  # By CSS
    _time_out = "thead tr .text-center:nth-of-type(4)"  # By CSS
    _time_spent = "thead tr .text-center:nth-of-type(5)"  # By CSS
    _break_time = "thead tr .text-center:nth-of-type(6)"  # By CSS
    _work_time = "thead tr .text-center:nth-of-type(7)"  # By CSS

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verifyLogs(self, detail, logs):
        db = self.dbGetElement(detail, logs)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyAbsentees(self, detail1, absentees):
        db = self.dbGetElement(detail1, absentees)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")

        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifySearchBar(self, detail2, searchbar):
        db = self.dbGetElement(detail2, searchbar)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self._search_bar, locatorType='css')
        return result

    def verifyMoreOptions(self, detail3, moreoptions):
        db = self.dbGetElement(detail3, moreoptions)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyAddNew(self, detail4, addnew):
        db = self.dbGetElement(detail4, addnew)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")

        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyExport(self, detail5, export):
        db = self.dbGetElement(detail5, export)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def waitForTable(self, detail6, table,):
        db = self.dbGetElement(detail6, table)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        self.waitForElement(self.locator, self.locatorType)

    def verifyTable(self, detail7, table1):
        db = self.dbGetElement(detail7, table1)
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

    def DetailsVerifyText(self, _text_day, _text_date, _text_time_in, _text_time_out, _text_time_spent, _text_break_time, _text_work_time, _text_absentees, _text_details, _text_logs, _text_add_new, _text_export):
        text = self.getText(self._day, locatorType='css')
        result = self.util.verifyTextContains(_text_day, text)
        self.stat.mark(result, "Verify Text Day ")
        text1 = self.getText(self._date, locatorType='css')
        result1 = self.util.verifyTextContains(_text_date, text1)
        self.stat.mark(result1, "Verify Text Date")
        text2 = self.getText(self._time_in, locatorType='css')
        result2 = self.util.verifyTextContains(_text_time_in, text2)
        self.stat.mark(result2, "Verify Text Time In")
        text3 = self.getText(self._time_out, locatorType='css')
        result3 = self.util.verifyTextContains(_text_time_out, text3)
        self.stat.mark(result3, "Verify Text Time Out")
        text4 = self.getText(self._time_spent, locatorType='css')
        result4 = self.util.verifyTextContains(_text_time_spent, text4)
        self.stat.mark(result4, "Verify Text Time Spent")
        text5 = self.getText(self._break_time, locatorType='css')
        result5 = self.util.verifyTextContains(_text_break_time, text5)
        self.stat.mark(result5, "Verify Text Break Time")
        text6 = self.getText(self._work_time, locatorType='css')
        result6 = self.util.verifyTextContains(_text_work_time, text6)
        self.stat.mark(result6, "Verify Text Work Time")
        text7 = self.getText(self._absentees, locatorType='link')
        result7 = self.util.verifyTextContains(_text_absentees, text7)
        self.stat.mark(result7, "Verify Text Absentees")
        text8 = self.getText(self._details, locatorType='link')
        result8 = self.util.verifyTextContains(_text_details, text8)
        self.stat.mark(result8, "Verify Text Details")
        text9 = self.getText(self._logs, locatorType='link')
        result9 = self.util.verifyTextContains(_text_logs, text9)
        self.stat.mark(result9, "Verify Text Logs")
        text10 = self.getText(self._add_new, locatorType='css')
        result10 = self.util.verifyTextContains(_text_add_new, text10)
        self.stat.mark(result10, "verify Text Add New")
        text11 = self.getText(self._export, locatorType='css')
        result11 = self.util.verifyTextContains(_text_export, text11)
        self.stat.mark(result11, "Verify Text Export")