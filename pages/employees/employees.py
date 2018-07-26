from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class Employees(BasePage):
    log = cl.customLogger(logging.DEBUG)
    locator = None
    locatorType = None

    # Locators
    _search_bar = "[type='text']"  # By CSS
    _new_employees = "New Employee"  # By Link
    _page_header = "//main[@id='wrapper']/div[@class='right-content']//strong[@class='text-dark']"  # By Xpath
    _title = "Cubix Inc"  # Title
    _employees = ".owl-stage div:nth-of-type(1) .emp-info"  # By CSS
    _active = ".owl-stage div:nth-of-type(2) .emp-info"  # By CSS
    _inactive = ".owl-stage div:nth-of-type(3) .emp-info"  # By CSS
    _full_time = ".owl-stage div:nth-of-type(4) .emp-info"  # By CSS
    _part_time = ".owl-stage div:nth-of-type(5) .emp-info"  # By CSS
    _probation = ".owl-stage div:nth-of-type(6) .emp-info"  # By CSS
    _contractual = ".owl-stage div:nth-of-type(7) .emp-info"  # By CSS
    _name = "thead tr th:nth-of-type(1)"  # By CSS
    _designation = "thead tr th:nth-of-type(2)"  # By CSS
    _department = "thead tr th:nth-of-type(3)"  # By CSS
    _location = "thead tr th:nth-of-type(4)"  # By CSS
    _status = "thead tr th:nth-of-type(5)"  # By CSS

    def __init__(self, driver):
        super().__init__(driver)

    def verifyPageheader(self, emp, employees):
        db = self.DBGetElement(emp, employees)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(emp, employees)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyNewEmployee(self, emp1, newemp):
        db = self.DBGetElement(emp1, newemp)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifySearchBar(self, emp2, searchbar):
        db = self.DBGetElement(emp2, searchbar)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def EmployeesSmoke(self, emp, pageheader, emp1, newemp, emp2, searchbar):
        self.nav.Employee()
        self.util.sleep(2)
        self.verifyPageTitle(self._title)
        result = self.verifyPageheader(emp, pageheader)
        self.stat.mark(result, "Verify Page Header")
        result1 = self.verifyNewEmployee(emp1, newemp)
        self.stat.mark(result1, "Verify New Employee")
        result2 = self.verifySearchBar(emp2, searchbar)
        self.stat.markFinal("Test_Employees Smoke", result2, "Verify Search Bar")

    def verifyTextEmployee(self, emp, newemp):
        db = self.DBGetElement(emp, newemp)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        exceptedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(emp, newemp)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText,exceptedText)
        return result

    def verifyTextName(self, emp1, name):
        db = self.DBGetElement(emp1, name)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        exceptedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(emp1, name)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, exceptedText)
        return result

    def verifyTextDesignation(self, emp2, designation):
        db = self.DBGetElement(emp2, designation)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        exceptedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(emp2, designation)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, exceptedText)
        return result

    def verifyTextDepartment(self, emp3, depart):
        db = self.DBGetElement(emp3, depart)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        exceptedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(emp3, depart)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, exceptedText)
        return result

    def verifyTextLocation(self, emp4, location):
        db = self.DBGetElement(emp4, location)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        exceptedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(emp4, location)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, exceptedText)
        return result

    def verifyTextStatus(self, emp5, status):
        db = self.DBGetElement(emp5, status)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        exceptedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(emp5, status)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, exceptedText)
        return result

    def TextEmployee(self, emp, newemp, emp1, name, emp2, designation, emp3, department, emp4, location, emp5, status):
        result = self.verifyTextEmployee(emp, newemp)
        self.stat.mark(result, "Verify Text Employees")
        result1 = self.verifyTextName(emp1, name)
        self.stat.mark(result1, "Verify Text Name")
        result2 = self.verifyTextDesignation(emp2, designation)
        self.stat.mark(result2, "Verify Text Designation")
        result3 = self.verifyTextDepartment(emp3, department)
        self.stat.mark(result3, "Verify Text Department")
        result4 = self.verifyTextLocation(emp4, location)
        self.stat.mark(result4, "Verify Text Location")
        result5 = self.verifyTextStatus(emp5, status)
        self.stat.markFinal("Test_Text Employees", result5, "Verify Text Status")