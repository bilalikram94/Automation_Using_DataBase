from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class SupportTicket(BasePage):
    log = cl.customLogger(logging.DEBUG)
    locator = None
    locatorType = None

    def __init__(self, driver):
        super().__init__(driver)

    def verifyMyTickets(self, support, tickets):
        db = self.DBGetElement(support, tickets)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column name incorrect !!!")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyCompanyTickets(self, support1, company):
        db = self.DBGetElement(support1, company)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column name incorrect !!!")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifySearchBar(self, support2, search):
        db = self.DBGetElement(support2, search)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column name incorrect !!!")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyOpenTicket(self, support3, openT):
        db = self.DBGetElement(support3, openT)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column name incorrect !!!")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyTickets(self, support4, ticket):
        db = self.DBGetElement(support4, ticket)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column name incorrect !!!")
        result = self.isElementPresent(self.locator, self.locatorType)
        return result

    def verifyTextSupport(self, support5, textSupport):
        db = self.DBGetElement(support5, textSupport)
        try:
            self.locator = db[0]
            self.locatorType = db[1]
        except:
            self.log.error("### Table name or Column name incorrect !!!")
        expectedText = self.getText(self.locator, self.locatorType)
        db1 = self.DBText(support5, textSupport)
        actualText = db1[0]
        result = self.util.verifyTextContains(actualText, expectedText)
        return result

    def SupportTicketSmoke(self, support, tickets, support1, company, support2, search, support3, openT, support4,
                           ticket, support5, textSupport):
        self.nav.SupportTicket()
        time.sleep(5)
        result = self.verifyMyTickets(support, tickets)
        self.stat.mark(result, "Verify My Tickets")
        result1 = self.verifyCompanyTickets(support1, company)
        self.stat.mark(result1, "Verify Company Tickets")
        result2 = self.verifySearchBar(support2, search)
        self.stat.mark(result2, "Verify Search Bar")
        result3 = self.verifyOpenTicket(support3, openT)
        self.stat.mark(result3, "Verify Open Ticket")
        result4 = self.verifyTickets(support4, ticket)
        self.stat.mark(result4, "Verify Tickets")
        result5 = self.verifyTextSupport(support5, textSupport)
        self.stat.markFinal("Test_Support Ticket", result5, "Verify Support Text")
