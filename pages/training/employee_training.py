from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class Training(BasePage):
    log = cl.customLogger(logging.DEBUG)
    locator = None
    locatorType = None

    # Locators
    _title = "Advanced HRMS - Staging"
    _search_bar = "//div[@id='basic_search']/input[@type='text']"  # By Xpath
    _page_title = ".page-title"  # By CSS
    _employee_training = "Employee Training"  # By Link
    _training_evaluation = "Training Evaluations"  # By Link
    _trainers = "Trainers"  # By Link
    _training_events = "Training Events"  # By Link
    _training_needs_assessment = "Training Needs Assessment"  # By Link
    _add_new_training = ".flex-v-middle .btn-action"  # By CSS
    _training_type = "thead tr th:nth-of-type(1)"  # By CSS
    _table_title = "thead tr th:nth-of-type(2)"  # By CSS
    _training_from = "thead tr th:nth-of-type(3)"  # By CSS
    _training_to = "thead tr th:nth-of-type(4)"  # By CSS
    _actions = "thead .text-right"  # By CSS
    _more_options = "tbody tr:nth-of-type(1) .dropdown"  # By CSS

    def __init__(self, driver):
        super().__init__(driver)

    def verifySearchbar(self, train, search):
        db = self.dbGetElement(train, search)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column name incorrect !!!")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyTextTitlePage(self, train1, page):
        db = self.dbGetElement(train1, page)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column Name Incorrect !!!")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(train1, page)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextEmployeeTraining(self, train2, emptrain):
        db = self.dbGetElement(train2, emptrain)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column Name Incorrect !!!")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(train2, emptrain)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextTrainingEvaluation(self, train3, evaluation):
        db = self.dbGetElement(train3, evaluation)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column Name Incorrect !!!")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(train3, evaluation)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextTrainers(self, train4, trainers):
        db = self.dbGetElement(train4, trainers)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column Name Incorrect !!!")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(train4, trainers)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextTrainingEvents(self, train5, events):
        db = self.dbGetElement(train5, events)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column Name Incorrect !!!")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(train5, events)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextTrainingNeedsAssessment(self, train6, assess):
        db = self.dbGetElement(train6, assess)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column Name Incorrect !!!")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(train6, assess)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextAddNewTraining(self, train7, training):
        db = self.dbGetElement(train7, training)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column Name Incorrect !!!")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(train7, training)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextTrainingType(self, train8, traintype):
        db = self.dbGetElement(train8, traintype)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column Name Incorrect !!!")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(train8, traintype)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextTableTitle(self, train9, table):
        db = self.dbGetElement(train9, table)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column Name Incorrect !!!")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(train9, table)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextTrainingFrom(self, train10, train_frm):
        db = self.dbGetElement(train10, train_frm)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column Name Incorrect !!!")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(train10, train_frm)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextTrainingTo(self, train11, train_to):
        db = self.dbGetElement(train11, train_to)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column Name Incorrect !!!")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(train11, train_to)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyTextActions(self, train12, actions):
        db = self.dbGetElement(train12, actions)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column Name Incorrect !!!")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(train12, actions)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def verifyMoreOptions(self, train13, more_options):
        db = self.dbGetElement(train13, more_options)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column name Incorrect !!!")
        result = self.isElementPresent(self._more_options, locatorType='css')
        return result

    def EmployeeTrainingSmoke(self, train, search, train1, page, train2, emptrain, train3, evaluation, train4, trainers,
                              train5, events, train6, assess, train7, training, train8, traintype, train9, table,
                              train10, train_frm, train11, train_to, train12, actions, train13, more_options):
        self.nav.Training()
        result = self.verifySearchbar(train, search)
        self.stat.mark(result, "Verify Search Bar")
        result1 = self.verifyTextTitlePage(train1, page)
        self.stat.mark(result1, "Verify Text Title Page")
        result2 = self.verifyTextEmployeeTraining(train2, emptrain)
        self.stat.mark(result2, "Verify Text Employee Training")
        result3 = self.verifyTextTrainingEvaluation(train3, evaluation)
        self.stat.mark(result3, "Verify Text Training Evaluation")
        result4 = self.verifyTextTrainers(train4, trainers)
        self.stat.mark(result4, "Verify Text Trainers")
        result5 = self.verifyTextTrainingEvents(train5, events)
        self.stat.mark(result5, "Verify Text Training Events")
        result6 = self.verifyTextTrainingNeedsAssessment(train6, assess)
        self.stat.mark(result6, "Verify Text Training Needs Assessment")
        result7 = self.verifyTextAddNewTraining(train7, training)
        self.stat.mark(result7, "Verify Text Add New Training")
        result8 = self.verifyTextTrainingType(train8, traintype)
        self.stat.mark(result8, "Verify Text Training Type")
        result9 = self.verifyTextTableTitle(train9, table)
        self.stat.mark(result9, "Verify Table Title")
        result10 = self.verifyTextTrainingFrom(train10, train_frm)
        self.stat.mark(result10, "Verify Text Training From")
        result11 = self.verifyTextTrainingTo(train11, train_to)
        self.stat.mark(result11, "Verify Text Training To")
        result12 = self.verifyTextActions(train12, actions)
        self.stat.mark(result12, "Verify Text Actions")
        result13 = self.verifyMoreOptions(train13, more_options)
        self.stat.markFinal("Test Employee Training", result13, "Verify More Options")