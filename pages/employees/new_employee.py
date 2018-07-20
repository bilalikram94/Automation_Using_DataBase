from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class NewEmployee(BasePage):
    log = cl.customLogger(logging.DEBUG)
    locator = None
    locatorType = None

    # Locators
    _first_name = "//main[@id='wrapper']//div[@class='container']/div[@class='row']//form[@role='form']//input[@name='fname']"  # Xpath
    _last_name = "//main[@id='wrapper']//div[@class='container']/div[@class='row']//form[@role='form']//input[@name='lname']"  # By Xpath
    _employee_card = "//main[@id='wrapper']//div[@class='container']/div[@class='row']//form[@role='form']//input[@name='employee_code']"  # By Xpath
    _gender = "//main[@id='wrapper']//div[@class='container']/div[@class='row']/div[@class='col-lg-10']/form[@role='form']/div[1]/div[@class='panel-body']/div[3]/div[1]/span//span[@role='combobox']"  # By Xpath
    _date_of_joining = "//main[@id='wrapper']//div[@class='container']/div[@class='row']//form[@role='form']//input[@name='doj']"  # By Xpath
    _department = "select2-department_id-container"  # By ID
    _designation = "select2-designation-container"  # By ID
    _reporting_person = ".select2-selection--multiple .select2-selection__rendered"  # By CSS
    _tax_rule = ".add-employee-form .row:nth-of-type(2) [class='col-md-5 form-group']:nth-of-type(2) .select2-selection__rendered"  # By CSS
    _user_role = ".add-employee-form .panel:nth-of-type(2) .row:nth-of-type(3) .select2-selection--single"  # By CSS
    _policy_type = ".add-employee-form .panel:nth-of-type(3) .select2-selection__rendered"  # By CSS
    _page_title = "Advanced HRMS - Staging"

    def __init__(self, driver):
        super().__init__(driver)

    def verifyFirstName(self, newemp, name):
        db = self.dbGetElement(newemp, name)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyLastName(self, newemp1, lname):
        db = self.dbGetElement(newemp1, lname)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyEmployeeCard(self, newemp2, empcard):
        db = self.dbGetElement(newemp2, empcard)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyGender(self, newemp3, gender):
        db = self.dbGetElement(newemp3, gender)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyDateOfJoining(self, newemp4, doj):
        db = self.dbGetElement(newemp4, doj)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyDepartment(self, newemp5, depart):
        db = self.dbGetElement(newemp5, depart)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyDesignation(self, newemp6, design):
        db = self.dbGetElement(newemp6, design)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyReportingPerson(self, newemp7, report):
        db = self.dbGetElement(newemp7, report)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyTaxRule(self, newemp8, tax):
        db = self.dbGetElement(newemp8, tax)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyUserRole(self, newemp9, urole):
        db = self.dbGetElement(newemp9, urole)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        self.scrollIntoView(self.locator, self.locatorType)
        self.util.sleep(3)
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyPolicyType(self, newemp10, policy):
        db = self.dbGetElement(newemp10, policy)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("Something went wrong")
        self.scrollIntoView(self.locator, self.locatorType)
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def NewEmployeeSmoke(self, newemp, name, newemp1, lname, newemp2, empcard, newemp3, gender, newemp4, doj, newemp5,
                         depart, newemp6, design, newemp7, report, newemp8, tax, newemp9, urole, newemp10, policy):
        self.nav.NewEmployee()
        self.verifyPageTitle(self._page_title)
        result = self.verifyFirstName(newemp, name)
        self.stat.mark(result, "Verify First Name")
        result1 = self.verifyLastName(newemp1, lname)
        self.stat.mark(result1, "Verify Last Name")
        result2 = self.verifyEmployeeCard(newemp2, empcard)
        self.stat.mark(result2, "Verify Employee Card")
        result3 = self.verifyGender(newemp3, gender)
        self.stat.mark(result3, "Verify Gender")
        result4 = self.verifyDateOfJoining(newemp4, doj)
        self.stat.mark(result4, "Verify Date Of Joining")
        result5 = self.verifyDepartment(newemp5, depart)
        self.stat.mark(result5, "Verify Department")
        result6 = self.verifyDesignation(newemp6, design)
        self.stat.mark(result6, "Verify Designation")
        result7 = self.verifyReportingPerson(newemp7, report)
        self.stat.mark(result7, "Verify Reporting Person")
        result8 = self.verifyTaxRule(newemp8, tax)
        self.stat.mark(result8, "Verify Tax Rule")
        result9 = self.verifyUserRole(newemp9, urole)
        self.stat.mark(result9, "Verify User Role")
        result10 = self.verifyPolicyType(newemp10, policy)
        self.stat.markFinal("Test New Employee", result10, "Verify Policy Type")